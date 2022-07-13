if __name__ == '__main__':
    INF = 1e9
    N = int(input())
    road = list(input())
    dp = [INF] * N
    dp[0] = 0

    for i in range(N):
        if dp[i] == INF:
            continue
        for j in range(i + 1, N):
            if (road[i] == 'B' and road[j] == 'O') or \
                    (road[i] == 'O' and road[j] == 'J') or \
                    (road[i] == 'J' and road[j] == 'B'):
                dp[j] = min((j - i) ** 2 + dp[i], dp[j])

    print(dp[N - 1] if dp[N - 1] != INF else -1)
