import sys
from collections import deque


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    space = []
    for _ in range(N):
        space.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    Q = deque()
    Q.append((0, 0))

    for i in range(N):
        for j in range(N):
            if i == j == N - 1:
                break
            jump = space[i][j]
            # y axis
            if i + jump < N:
                dp[i + jump][j] += dp[i][j]
            # x axis
            if j + jump < N:
                dp[i][j + jump] += dp[i][j]

    print(dp[N - 1][N - 1])
