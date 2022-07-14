if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = [[0] * (20 + 1) for _ in range(N)]
    dp[0][numbers[0]] = 1

    for i in range(N - 2):
        for j in range(20 + 1):
            if not dp[i][j]:
                continue

            plus = j + numbers[i + 1]
            minus = j - numbers[i + 1]
            if 0 <= plus <= 20:
                dp[i + 1][plus] += dp[i][j]
            if 0 <= minus <= 20:
                dp[i + 1][minus] += dp[i][j]

    print(dp[N - 2][numbers[-1]])
