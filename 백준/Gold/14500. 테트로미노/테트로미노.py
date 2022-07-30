from typing import *
import sys

TETS = ((1, 0), (0, 1), (0, -1))
TETS_T = (
    ((-1, -1), (-1, 0), (-1, 1)),
    ((-1, -1), (0, -1), (1, -1)),
    ((1, -1), (1, 0), (1, 1)),
    ((-1, 1), (0, 1), (1, 1))
)


res: int = 0

if __name__ == '__main__':
    def dfs(y: int, x: int, level: int, covered: int) -> None:
        if level == 4:
            global res
            res = max(res, covered)
            return

        for idx, (dy, dx) in enumerate(TETS):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx, level + 1, covered + field[ny][nx])
                visited[ny][nx] = False


    N, M = list(map(int, input().split()))
    visited: List[List[bool]] = [[False] * M for _ in range(N)]
    finished: List[List[bool]] = [[False] * M for _ in range(N)]
    field: List[List[int]] = []

    for _ in range(N):
        line = sys.stdin.readline().split()
        field.append(list(map(int, line)))

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, field[i][j])
            visited[i][j] = False

            for t in TETS_T:
                is_intact = True
                t_sum = field[i][j]
                for di, dj in t:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        t_sum += field[ni][nj]
                    else:
                        is_intact = False
                        break
                if is_intact:
                    res = max(res, t_sum)

    print(res)
