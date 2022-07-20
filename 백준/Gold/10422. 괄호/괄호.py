import sys

if __name__ == '__main__':
    dp = [0] * (5000 + 1)
    dp[0] = dp[2] = 1
    T = int(input())

    for i in range(4, 5000 + 1, 2):
        for j in range(2, i + 1, 2):
            dp[i] += dp[j - 2] * dp[i - j]
        dp[i] %= 1_000_000_007

    for _ in range(T):
        n = int(sys.stdin.readline())
        print(dp[n])
