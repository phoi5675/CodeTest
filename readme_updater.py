import os

PLATFORMS = ['백준', '프로그래머스']
README_PREFIX = \
    '''
# CodeTest

Repository for preparing coding test

Automatically pushed by [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)
# List of problems

| Platform | Level | Title | Description | code |
|----------|-------|-------|-------------|------|
'''
if __name__ == '__main__':

    table_contents = []
    for platform in PLATFORMS:
        levels = os.listdir('./' + platform)
        for level in levels:
            prob_dirs = os.listdir('./{0}/{1}'.format(platform, level))
            for prob_dir in prob_dirs:
                file_list = os.listdir('./{0}/{1}/{2}'.format(platform, level, prob_dir))
                code_file = next(c for c in file_list if c != 'README.md')
                readme = next(c for c in file_list if c == 'README.md')
                table_contents.append([
                    platform, level, prob_dir, prob_dir.replace('\u2005', ' ')[prob_dir.index('.') + 2:],
                    readme, code_file.replace('\u2005', ' ')
                ])

    table = []
    for content in table_contents:
        platform, level, prob_dir, prob, readme, code_file = content
        prob_path = './{0}/{1}/{2}'.format(platform, level, prob_dir).replace('\u2005', '%E2%80%85')
        code_path = prob_path + '/' + code_file.replace(' ', '%E2%80%85')
        table.append(f'|{platform}|{level}|{prob}|[README.md]({prob_path}/{readme}) \
            |[{code_file}]({code_path})|')

    with open('./README.md', 'w') as readme:
        readme.write(README_PREFIX)
        readme.write('\n'.join(table))
