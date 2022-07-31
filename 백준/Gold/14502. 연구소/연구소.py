from typing import *
from copy import deepcopy
from collections import deque
from itertools import combinations

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
EMPTY, WALL, VIRUS = 0, 1, 2

if __name__ == '__main__':
    res: int = 0
    n, m = list(map(int, input().split()))
    space: List[List[int]] = []
    visited: List[List[bool]] = [[False] * m for _ in range(n)]
    _visited = deepcopy(visited)
    zeroes: List[Tuple[int, int]] = []
    Q = deque()
    _Q = deque()

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == EMPTY:
                zeroes.append((i, j))
            elif line[j] == VIRUS:
                Q.append((i, j))
        space.append(line)

    _Q = deepcopy(Q)
    for combs in combinations(range(len(zeroes)), 3):
        for c in combs:
            space[zeroes[c][0]][zeroes[c][1]] = WALL
        visited = deepcopy(_visited)
        Q = deepcopy(_Q)
        safe_area: int = len(zeroes) - 3
        while Q:
            y, x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and \
                        space[ny][nx] == EMPTY:
                    visited[ny][nx] = True
                    Q.append((ny, nx))
                    safe_area -= 1

        for c in combs:
            space[zeroes[c][0]][zeroes[c][1]] = EMPTY
        res = max(res, safe_area)

    print(res)
