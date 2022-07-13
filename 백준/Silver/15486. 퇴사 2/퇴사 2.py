import sys

if __name__ == "__main__":

    task, price, dp = [], [], []
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b = list(map(int, sys.stdin.readline().split()))
        task.append(a)
        price.append(b)
        dp.append(b)
    dp.append(0)

    for i in range(n - 1, -1, -1):
        if i + task[i] > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], price[i] + dp[i + task[i]])

    print(dp[0])
