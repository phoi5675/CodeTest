import sys


if __name__ == '__main__':
    N, S, M = list(map(int, sys.stdin.readline().split()))
    V = list(map(int, sys.stdin.readline().split()))
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    res = -1

    # Init condition
    dp[0][S] = True

    for i in range(0, N):
        for j in range(0, M + 1):
            if not dp[i][j]:
                continue

            if j + V[i] <= M:
                dp[i + 1][j + V[i]] = True
            if j - V[i] >= 0:
                dp[i + 1][j - V[i]] = True

    for i in range(0, M + 1):
        if dp[N][i]:
            res = i

    print(res)
