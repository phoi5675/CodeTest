from typing import *

if __name__ == '__main__':
    string: List[str] = list(input())
    bomb: str = input()
    res: List[str] = []

    last_ch: str = bomb[-1]
    stack: List[str] = []

    for i, ch in enumerate(string):
        stack.append(ch)

        if ch == last_ch and len(stack) >= len(bomb):
            tmp: List[str] = []
            match: bool = True
            for j, bomb_ch in enumerate(bomb):
                stack_ch = stack.pop()
                tmp.append(stack_ch)
                if stack_ch != bomb[len(bomb) - (j + 1)]:
                    match = False

            if match:
                tmp.clear()
            else:
                res.extend(stack)
                res.extend(reversed(tmp))
                stack.clear()

    if stack:
        res.extend(stack)

    print(''.join(res) if res else 'FRULA')
