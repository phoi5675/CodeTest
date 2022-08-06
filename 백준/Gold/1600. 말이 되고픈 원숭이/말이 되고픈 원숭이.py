from typing import *
from collections import deque

HORSE_VEC = ((-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1))
VEC = ((1, 0), (-1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    k = int(input())
    w, h = list(map(int, input().split()))
    space: List[List[int]] = []
    visited: List[List[List[bool]]] = [[[False] * w for _ in range(h)] for _ in range(k + 1)]
    Q: Deque[Tuple[int, int, int, int]] = deque()
    Q.append((0, 0, 0, 0))

    for _ in range(h):
        space.append(list(map(int, input().split())))

    while Q:
        y, x, moves, horse_moves = Q.popleft()
        if y == h - 1 and x == w - 1:
            print(moves)
            exit(0)

        if horse_moves < k:
            for dy, dx in HORSE_VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and space[ny][nx] != 1 and not visited[horse_moves + 1][ny][nx]:
                    visited[horse_moves + 1][ny][nx] = True
                    Q.append((ny, nx, moves + 1, horse_moves + 1))

        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and space[ny][nx] != 1 and not visited[horse_moves][ny][nx]:
                visited[horse_moves][ny][nx] = True
                Q.append((ny, nx, moves + 1, horse_moves))

    print(-1)
