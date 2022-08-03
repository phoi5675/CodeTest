from typing import *
from collections import deque

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
LIMIT = 9
if __name__ == '__main__':
    def bfs(_Q: Deque[Tuple[int, int]], _visited: List[List[bool]]) -> None:
        while _Q:
            y, x = _Q.popleft()

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if not _visited[ny][nx] and water[ny][nx] > 0:
                        _Q.append((ny, nx))
                        _visited[ny][nx] = True
                    if 0 < y < n - 1 and 0 < x < m - 1:
                        if water[ny][nx] == 0 and pool[ny][nx] <= pool[y][x]:
                            water[y][x] = 0
                        elif water[y][x] + pool[y][x] > water[ny][nx] + pool[ny][nx]:
                            if pool[ny][nx] < pool[y][x] and not water[ny][nx] or \
                                    pool[y][x] > water[ny][nx] + pool[ny][nx]:
                                water[y][x] = 0
                            elif pool[ny][nx] < pool[y][x]:
                                water[y][x] = min(water[y][x], abs(pool[ny][nx] + water[ny][nx] - pool[y][x]))
                            else:
                                water[y][x] = min(water[y][x], abs(pool[ny][nx] - pool[y][x]) + water[ny][nx])

    n, m = list(map(int, input().split()))
    pool: List[List[int]] = [[0] * m for _ in range(n)]
    water: List[List[int]] = [[0] * m for _ in range(n)]
    max_height: int = 0
    Q: Deque[Tuple[int, int]] = deque()
    visited: List[List[bool]] = [[False] * m for _ in range(n)]

    for i in range(n):
        line = list(map(int, list(input())))
        for j in range(m):
            pool[i][j] = line[j]
            max_height = max(max_height, pool[i][j])
            # Visit edges first
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                Q.append((i, j))
                visited[i][j] = True
                water[i][j] = 0

    # Fill water first
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            water[i][j] = max_height - pool[i][j]

    bfs(Q, visited)

    is_leftover_exist = True
    while is_leftover_exist:
        is_leftover_exist = False
        Q.clear()
        # Fix leftovers
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if water[i][j] == 0:
                    continue
                for di, dj in VEC:
                    ni, nj = i + di, j + dj
                    if pool[i][j] + water[i][j] > pool[ni][nj] + water[ni][nj]:
                        is_leftover_exist = True
                        Q.append((i, j))
                        break
        bfs(Q, visited)

    print(sum(sum(w) for w in water))
