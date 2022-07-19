import re

if __name__ == '__main__':
    dec = input()

    inputs = dec.split()
    var_types, variables = [], []

    for v in inputs:
        res = re.findall('[,;]', v)
        if re.findall('[,;]', v):
            variables.append(re.sub('[,;]', '', v))
        else:
            var_types.append(v)

    for v in variables:
        name = re.sub('[^(a-zA-Z)]', '', v)
        typ = list(re.sub('[(a-zA-Z)]', '', v))
        typ_processed = []
        for t in reversed(typ):
            if t == '*':
                typ_processed.append('*')
            elif t == '&':
                typ_processed.append('&')
            elif t == '[':
                typ_processed.append('[]')

        print(f'{"".join(var_types)}{"".join(typ_processed)} {name};')
