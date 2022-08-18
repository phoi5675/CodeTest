import sys
from typing import *
from collections import deque

WATER, LAND = 0, 1
VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

res = 0

if __name__ == '__main__':
    def bfs(queue: Deque[Tuple[int, int, int]], y: int, x: int) -> int:
        local_max_route = 0
        queue.clear()
        queue.append((y, x, 0))
        visited[y][x][y][x] = True

        while Q:
            cur_y, cur_x, cur_dist = queue.popleft()
            local_max_route = max(local_max_route, cur_dist)

            for dy, dx in VEC:
                ny, nx = cur_y + dy, cur_x + dx
                if 0 <= ny < n and 0 <= nx < m and treasure_map[ny][nx] == LAND and not visited[y][x][ny][nx]:
                    visited[y][x][ny][nx] = True
                    queue.append((ny, nx, cur_dist + 1))

        return local_max_route
    n, m = map(int, input().split())
    treasure_map: List[List[int]] = [[WATER] * m for _ in range(n)]
    visited: List[List[List[List[bool]]]] = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    Q: Deque[Tuple[int, int, int]] = deque()

    for i in range(n):
        line: List[str] = list(sys.stdin.readline().strip())
        for j in range(m):
            treasure_map[i][j] = LAND if line[j] == 'L' else WATER

    for i in range(n):
        for j in range(m):
            if treasure_map[i][j] == LAND and not visited[i][j][i][j]:
                res = max(res, bfs(Q, i, j))

    print(res)
