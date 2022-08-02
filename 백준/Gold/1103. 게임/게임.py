from typing import *
import sys
sys.setrecursionlimit(10000)

VEC = ((1, 0), (-1, 0), (0, 1), (0, -1))
INF: int = int(1e9)

if __name__ == '__main__':
    def dfs(y: int, x: int) -> int:
        if (0 <= y < n and 0 <= x < m and board[y][x] == 'H') or \
                y < 0 or y >= n or x < 0 or x >= m:
            return 0
        if visited[y][x]:
            print(-1)
            exit(0)
        if dp[y][x] != -1:
            return dp[y][x]

        visited[y][x] = True
        dp[y][x] = 0

        for dy, dx in VEC:
            ny, nx = y + dy * int(board[y][x]), x + dx * int(board[y][x])
            dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

        visited[y][x] = False
        return dp[y][x]


    n, m = list(map(int, input().split()))
    dp: List[List[int]] = [[-1] * m for _ in range(n)]
    visited: List[List[bool]] = [[False] * m for _ in range(n)]
    board: List[List[str]] = []
    for _ in range(n):
        board.append(list(input()))

    print(dfs(0, 0))
