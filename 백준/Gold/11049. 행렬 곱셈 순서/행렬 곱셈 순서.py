import sys

if __name__ == '__main__':
    N = int(input())
    mats = []
    dp = [[0] * N for _ in range(N)]
    for _ in range(N):
        mats.append(list(map(int, sys.stdin.readline().split())))

    # 연쇄행렬 곱셈
    for r in range(2, N + 1):
        for i in range(N):
            j = i + r - 1
            if j >= N:
                break

            min_cost = mats[i][0] * mats[i][1] * mats[j][1] + dp[i][i] + dp[i + 1][j]
            for k in range(i + 1, j):
                min_cost = min(min_cost, dp[i][k] + dp[k + 1][j] + mats[i][0] * mats[j][1] * mats[k][1])

            dp[i][j] = min_cost

    print(dp[0][-1])
