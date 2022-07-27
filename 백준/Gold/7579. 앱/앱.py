from typing import *

MEM, COST = 0, 1
INF = int(1e9)
if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    apps: List[int] = list(map(int, input().split()))
    costs: List[int] = list(map(int, input().split()))
    dp_range = sum(costs)
    dp: List[List[List[int]]] = [[[0, 0] for _ in range(dp_range + 1)] for _ in range(N + 1)]
    res: int = INF

    for i in range(1, N + 1):
        for j in range(1, dp_range + 1):
            if costs[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j][COST] = max(dp[i - 1][j][COST], costs[i - 1] + dp[i - 1][j - costs[i - 1]][COST])
                dp[i][j][MEM] = max(dp[i - 1][j][MEM], apps[i - 1] + dp[i - 1][j - costs[i - 1]][MEM])

            if dp[i][j][MEM] >= M:
                res = min(res, dp[i][j][COST])

    print(res)
