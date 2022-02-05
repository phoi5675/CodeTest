import sys

if __name__ == "__main__":
    def recursive(index: int) -> int:
        traversed = []

        for i in range(index, n):
            if i + task[i] <= n:
                traversed.append(price[i] + recursive(i + task[i]))

        if traversed:
            return max(traversed)
        else:
            return 0

    task, price = [], []
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b = list(map(int, sys.stdin.readline().split()))
        task.append(a)
        price.append(b)

    res = 0

    for i in range(n):
        if i + task[i] <= n:
            res = max(res, price[i] + recursive(i + task[i]))

    print(res)
