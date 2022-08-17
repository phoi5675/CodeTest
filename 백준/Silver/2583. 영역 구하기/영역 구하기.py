from typing import *
from collections import deque

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    def bfs(y: int, x: int) -> int:
        Q = deque()
        cur_area = 1
        Q.append((y, x))
        paper[y][x] = True

        while Q:
            cur_y, cur_x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = cur_y + dy, cur_x + dx
                if 0 <= ny < n and 0 <= nx < m and not paper[ny][nx]:
                    Q.append((ny, nx))
                    paper[ny][nx] = True
                    cur_area += 1

        return cur_area

    n, m, k = map(int, input().split())
    paper: List[List[bool]] = [[False] * m for _ in range(n)]
    spaces: List[int] = []
    for _ in range(k):
        ux, uy, dx, dy = map(int, input().split())
        for i in range(uy, dy):
            for j in range(ux, dx):
                paper[i][j] = True

    for i in range(n):
        for j in range(m):
            if not paper[i][j]:
                spaces.append(bfs(i, j))

    print(len(spaces))
    print(*sorted(spaces), sep=' ')
