from typing import *

if __name__ == '__main__':
    n = int(input())
    wines: List[int] = []
    dp: List[List[int]] = [[0] * 2 for _ in range(n)]
    for _ in range(n):
        wines.append(int(input()))

    if n <= 2:
        print(sum(wines))
        exit(0)

    dp[0][0] = wines[0]
    dp[0][1] = wines[0]
    dp[1][0] = wines[1]
    dp[1][1] = wines[0] + wines[1]
    prev_max = wines[0]

    for i in range(1, n - 1):
        if i >= 2:
            dp[i + 1][0] = prev_max + wines[i + 1]
        else:
            dp[i + 1][0] = dp[i - 1][1] + wines[i + 1]
        dp[i + 1][1] = dp[i][0] + wines[i + 1]
        prev_max = max(prev_max, *dp[i])

    print(max(max(dp_line) for dp_line in dp))
