WEIGHT, VALUE = 0, 1
if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    things = [(0, 0)]
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    for _ in range(N):
        things.append(tuple(map(int, input().split())))

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if things[i][WEIGHT] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], things[i][VALUE] + dp[i - 1][j - things[i][WEIGHT]])

    print(dp[-1][-1])
