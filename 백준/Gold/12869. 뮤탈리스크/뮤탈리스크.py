from typing import *

INF = int(1e9)

if __name__ == '__main__':
    def recursive(a: int, b: int, c: int) -> int:
        if a < 0:
            return recursive(0, b, c)
        if b < 0:
            return recursive(a, 0, c)
        if c < 0:
            return recursive(a, b, 0)

        if a == 0 and b == 0 and c == 0:
            return 0

        if dp[a][b][c] != -1:
            return dp[a][b][c]

        dp[a][b][c] = INF
        dp[a][b][c] = min(dp[a][b][c], recursive(a - 9, b - 3, c - 1) + 1)
        dp[a][b][c] = min(dp[a][b][c], recursive(a - 9, b - 1, c - 3) + 1)

        dp[a][b][c] = min(dp[a][b][c], recursive(a - 3, b - 9, c - 1) + 1)
        dp[a][b][c] = min(dp[a][b][c], recursive(a - 1, b - 9, c - 3) + 1)

        dp[a][b][c] = min(dp[a][b][c], recursive(a - 1, b - 3, c - 9) + 1)
        dp[a][b][c] = min(dp[a][b][c], recursive(a - 3, b - 1, c - 9) + 1)

        return dp[a][b][c]

    N = int(input())
    SCVs = list(map(int, input().split()))
    dp: List[List[List[int]]] = [[[-1] * 61 for _ in range(61)] for _ in range(61)]

    SCVs.extend([0] * (3 - N))

    print(recursive(*SCVs))
