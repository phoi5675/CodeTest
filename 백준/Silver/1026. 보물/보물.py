INF = 1e9

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort(reverse=True)

    res = 0
    for a, b in zip(A, B):
        res += a * b

    print(res)
