import os
from typing import *

PLATFORMS = ['백준', '프로그래머스']
README_PREFIX = \
    '''
# CodeTest

Repository for preparing coding test

Automatically pushed by [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)
# List of problems
| Platform | Level | Title | Code |
|----------|-------|-------|------|
'''
STYLES = \
    '''<style>
img{
    width: 20px;
    height: 20px;
}
</style>'''
if __name__ == '__main__':

    table_contents: List[List[str]] = []
    for platform in PLATFORMS:
        levels = os.listdir('./' + platform)
        for level in levels:
            prob_dirs = os.listdir('./{0}/{1}'.format(platform, level))
            for prob_dir in prob_dirs:
                file_list = os.listdir('./{0}/{1}/{2}'.format(platform, level, prob_dir))
                code_files = [c for c in file_list if c != 'README.md']
                readme = next(c for c in file_list if c == 'README.md')
                table_contents.append([
                    platform, level, prob_dir, prob_dir.replace('\u2005', ' ')[prob_dir.index('.') + 2:],
                    readme, [c.replace('\u2005', ' ') for c in code_files]
                ])

    table = []
    for content in table_contents:
        platform, level, prob_dir, prob, readme, code_files = content
        prob_path = './{0}/{1}/{2}'.format(platform, level, prob_dir).replace('\u2005', '%E2%80%85')
        code_file_tags = [f'[<img src=./icons/{c[c.rfind(".") + 1:]}.png alt="{c}" />]' \
                          f'({prob_path + "/" + c.replace(" ", "%E2%80%85")})' for c in code_files]
        table.append(f'|{platform}|{level}|[{prob}]({prob_path}/{readme}) \
            |{" ".join(code_file_tags)}|')

    with open('./README.md', 'w') as readme:
        readme.write(STYLES)
        readme.write(README_PREFIX)
        readme.write('\n'.join(table))
