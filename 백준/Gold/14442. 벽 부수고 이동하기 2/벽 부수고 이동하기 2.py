from typing import *
from collections import deque

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
EMPTY, WALL = 0, 1
MAXIMUM_BREACH_ABLE = 10

if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    space: List[List[int]] = []
    visited: List[List[List[bool]]] = [[[False] * m for _ in range(n)] for _ in range(MAXIMUM_BREACH_ABLE + 1)]
    Q: Deque[Tuple[int, int, int, int]] = deque()

    for _ in range(n):
        space.append(list(map(int, list(input()))))

    Q.append((0, 0, 1, 0))
    visited[0][0][0] = True

    while Q:
        y, x, moves, breached = Q.popleft()
        if y == n - 1 and x == m - 1:
            print(moves)
            exit(0)

        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if space[ny][nx] == EMPTY and not visited[breached][ny][nx]:
                    visited[breached][ny][nx] = True
                    Q.append((ny, nx, moves + 1, breached))
                elif space[ny][nx] == WALL and breached < k and not visited[breached + 1][ny][nx]:
                    visited[breached + 1][ny][nx] = True
                    Q.append((ny, nx, moves + 1, breached + 1))

    print(-1)