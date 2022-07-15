INF = int(1e9)

if __name__ == '__main__':
    def recursive(idx: int) -> int:
        if dp[idx] < INF:
            return dp[idx]

        remain = M - names[idx]
        for i in range(idx + 1, N + 1):
            if remain < 0:
                break
            if i == N:
                dp[idx] = 0
                break

            dp[idx] = min(dp[idx], remain ** 2 + recursive(i))
            remain -= names[i] + 1

        return dp[idx]

    N, M = list(map(int, input().split()))
    names = []
    dp = [INF] * N
    dp[N - 1] = 0
    for _ in range(N):
        names.append(int(input()))

    print(recursive(0))
