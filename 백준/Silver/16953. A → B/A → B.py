import sys

INF = 1e9

if __name__ == '__main__':
    def dfs(num: int, level: int) -> None:
        global res
        if num == B:
            res = min(res, level + 1)
        elif num > B:
            return

        dfs(num << 1, level + 1)
        dfs(num * 10 + 1, level + 1)

    A, B = list(map(int, sys.stdin.readline().split()))
    res = INF

    dfs(A, 0)

    print(res if res != INF else -1)
