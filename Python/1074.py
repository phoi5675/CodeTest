if __name__ == '__main__':
    N, r, c = list(map(int, input().split()))

    res = 0

    for i in range(N - 1, 0 - 1, -1):
        boundary = 2 ** i
        if 0 <= r < boundary and 0 <= c < boundary:
            multiplier = 0
        elif 0 <= r < boundary and boundary <= c < 2 * boundary:
            multiplier = 1
        elif boundary <= r < 2 * boundary and 0 <= c < boundary:
            multiplier = 2
        else:
            multiplier = 3

        res += (boundary ** 2) * multiplier
        if r >= boundary:
            r -= boundary
        if c >= boundary:
            c -= boundary

    print(res)
