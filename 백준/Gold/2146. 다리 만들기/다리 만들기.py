import sys
from typing import *
from copy import deepcopy
from collections import deque
sys.setrecursionlimit(11000)

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
INF = int(1e9)
INIT_ISLAND = -1
SEA = 0

if __name__ == '__main__':
    def dfs(y: int, x: int, island_num: int) -> None:
        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and space[ny][nx] == INIT_ISLAND:
                space[ny][nx] = island_num
                dfs(ny, nx, island_num)

    def bfs(y: int, x: int) -> None:
        cur_minimum_len = bridges[space[y][x]]
        Q = deque()
        Q.append((y, x, 0))
        visited[y][x] = True

        while Q:
            _y, _x, moves = Q.popleft()
            if moves >= cur_minimum_len:
                break

            for dy, dx in VEC:
                ny, nx = _y + dy, _x + dx
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                    if space[ny][nx] == SEA:
                        visited[ny][nx] = True
                        Q.append((ny, nx, moves + 1))
                    elif space[ny][nx] != SEA and space[y][x] != space[ny][nx]:
                        bridges[space[y][x]] = min(bridges[space[y][x]], moves)
                        bridges[space[ny][nx]] = min(bridges[space[ny][nx]], moves)
                        return

    def is_near_sea(y: int, x: int) -> bool:
        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and space[ny][nx] == SEA:
                return True
        return False

    n = int(input())
    num_of_islands: int = 0
    space: List[List[int]] = []
    visited: List[List[bool]] = [[False] * n for _ in range(n)]
    _visited = deepcopy(visited)

    for i in range(n):
        line: List[int] = list(map(int, input().split()))
        for j, pos in enumerate(line):
            line[j] = INIT_ISLAND if pos else line[j]
        space.append(line)

    # Make island clusters.
    for i in range(n):
        for j in range(n):
            if space[i][j] == INIT_ISLAND:
                num_of_islands += 1
                space[i][j] = num_of_islands
                dfs(i, j, num_of_islands)

    bridges: List[int] = [INF] * (num_of_islands + 1)
    # Make bridges
    for i in range(n):
        for j in range(n):
            if space[i][j] and is_near_sea(i, j):
                visited = deepcopy(_visited)
                bfs(i, j)

    print(min(bridges))
