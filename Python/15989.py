import sys


if __name__ == '__main__':
    T = int(input())
    dp = [[0] * 4 for _ in range(10000 + 1)]
    dp[1] = [0, 1, 0, 0]
    dp[2] = [0, 1, 1, 0]
    dp[3] = [0, 1, 1, 1]
    for i in range(4, 10000 + 1):
        dp[i][1] = 1
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
        dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3]

    for _ in range(T):
        print(sum(dp[int(sys.stdin.readline())]))
