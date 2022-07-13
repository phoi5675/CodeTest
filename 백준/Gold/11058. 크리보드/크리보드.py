if __name__ == '__main__':
    N = int(input())
    dp = [0 for _ in range(100 + 1)]

    # Initialize
    for i in range(0 + 1, 6 + 1):
        dp[i] = i

    for i in range(7, N + 1):
        for j in range(1, i - 3):
            dp[i] = max(dp[i], dp[i - 1] + 1, (j + 1) * dp[i - (j + 2)])

    print(dp[N])
