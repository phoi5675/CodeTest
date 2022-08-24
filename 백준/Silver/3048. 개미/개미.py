from typing import *

LEFT, RIGHT = 0, 1

if __name__ == '__main__':
    def recursive(arr: List[str], idx: int, level: int, offset: int) -> None:
        if level == t or not 0 < idx < len(arr) or (0 < idx < len(arr) and vec[idx] == vec[idx - 1]):
            return

        arr[idx - 1], arr[idx] = arr[idx], arr[idx - 1]
        vec[idx - 1], vec[idx] = vec[idx], vec[idx - 1]

        recursive(arr, idx + offset, level + 1, offset)

    n1, n2 = map(int, input().split())
    ant_1 = list(reversed((input())))
    ant_2 = list(input())
    t = int(input())

    ans = []
    ans.extend(ant_1)
    ans.extend(ant_2)
    vec: List[int] = [LEFT] * len(ant_1) + [RIGHT] * len(ant_2)

    for i in range(t):
        if len(ant_1) < len(ant_2):
            recursive(ans, len(ant_1) + i, i, -1)
        else:
            recursive(ans, len(ant_1) - i, i, +1)

    print(''.join(ans))
