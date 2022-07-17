if __name__ == '__main__':
    N = int(input())
    trains = [0]

    trains.extend(list(map(int, input().split())))
    capacity = int(input())

    # Calculate expected capacity of towed train
    sums = [0] * (N + 1)
    sums[1] = sum(trains[1:capacity + 1])
    dp = [[0] * (N + 1) for _ in range(3 + 1)]

    for i in range(2, N - (capacity - 1) + 1):
        sums[i] = -trains[i - 1] + sums[i - 1] + trains[i + (capacity - 1)]

    for i in range(1, 3 + 1):
        for j in range(i * capacity, N + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - capacity] + sums[j - (capacity - 1)])

    print(dp[3][-1])
