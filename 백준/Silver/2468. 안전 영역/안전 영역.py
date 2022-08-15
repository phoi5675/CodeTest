from typing import *
from collections import deque

HEIGHT_LIMIT = 100 + 1

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    def bfs(y: int, x: int, height: int) -> None:
        Q: Deque[Tuple[int, int]] = deque()
        Q.append((y, x))
        visited[height][y][x] = True

        while Q:
            cur_y, cur_x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = cur_y + dy, cur_x + dx
                if 0 <= ny < n and 0 <= nx < n and not visited[height][ny][nx] and height_map[ny][nx] > height:
                    visited[height][ny][nx] = True
                    Q.append((ny, nx))

    n = int(input())
    safe_area: int = 0
    height_map: List[List[int]] = []
    visited: List[List[List[bool]]] = [[[False] * n for _ in range(n)] for _ in range(HEIGHT_LIMIT)]
    maximum_height: int = 0

    for _ in range(n):
        line = list(map(int, input().split()))
        maximum_height = max(maximum_height, *line)
        height_map.append(line)

    for height in range(maximum_height, 0, -1):
        cur_safe_area = 0
        for i in range(n):
            for j in range(n):
                if visited[height][i][j] or height_map[i][j] <= height:
                    continue
                bfs(i, j, height)
                cur_safe_area += 1
        safe_area = max(safe_area, cur_safe_area)

    print(safe_area if safe_area else 1)
