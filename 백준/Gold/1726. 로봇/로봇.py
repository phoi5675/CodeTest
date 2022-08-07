from typing import *
from collections import deque

VEC = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0))
E, W, S, N = 1, 2, 3, 4

if __name__ == '__main__':
    def turns(_heading: int) -> tuple:
        if _heading == E or _heading == W:
            return 3, 4
        else:
            return 1, 2

    m, n = list(map(int, input().split()))
    factory: List[List[int]] = []
    visited: List[List[List[bool]]] = [[[False] * n for _ in range(m)] for _ in range(5)]
    Q: Deque = deque()

    for _ in range(m):
        factory.append(list(map(int, input().split())))

    init_status: List[int] = list(map(int, input().split()))
    dst_status: List[int] = list(map(int, input().split()))

    # Make 0-indexed
    init_status[0] -= 1
    init_status[1] -= 1
    dst_status[0] -= 1
    dst_status[1] -= 1

    Q.append((*init_status, 0))
    visited[init_status[2]][init_status[0]][init_status[1]] = True

    while Q:
        y, x, heading, moves = Q.popleft()

        if y == dst_status[0] and x == dst_status[1]:
            offset = 0
            dst_heading = dst_status[2]
            if heading == dst_heading:
                offset = 0
            elif 1 <= heading <= 2 and 1 <= dst_heading <= 2 or \
                    3 <= heading <= 4 and 3 <= dst_heading <= 4:
                offset = 2
            else:
                offset = 1
            print(moves + offset)
            exit(0)

        for i in range(1, 3 + 1):
            ny, nx = y + VEC[heading][0] * i, x + VEC[heading][1] * i
            if 0 <= ny < m and 0 <= nx < n:
                if not visited[heading][ny][nx] and factory[ny][nx] == 0:
                    visited[heading][ny][nx] = True
                    Q.append((ny, nx, heading, moves + 1))
                elif factory[ny][nx] == 1:
                    break

        new_turns = turns(heading)

        for turn in new_turns:
            if not visited[turn][y][x]:
                visited[turn][y][x] = True
                Q.append((y, x, turn, moves + 1))
