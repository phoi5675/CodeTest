if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    num_of_commons = 0
    res = 0

    for i in range(1, N + 1):
        if N % i == 0:
            num_of_commons += 1
        if num_of_commons == K:
            res = i
            break

    print(res)
