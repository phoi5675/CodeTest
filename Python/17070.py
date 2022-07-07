import sys


R, BR, B = 0, 1, 2
VEC = ((0, 1), (1, 1), (1, 0))
VEC_DICT = {
    R: (R, BR),
    BR: (R, BR, B),
    B: (BR, B),
}
EMPTY, WALL = 0, 1

if __name__ == '__main__':
    def dfs(y: int, x: int, vec: int) -> None:
        global res
        if y == N - 1 and x == N - 1:
            res += 1
            return
        if y >= N or x >= N:
            return

        if vec == R or vec == BR:
            if x < N - 1 and not space[y][x + 1]:
                dfs(y, x + 1, R)
        if vec == B or vec == BR:
            if y < N - 1 and not space[y + 1][x]:
                dfs(y + 1, x, B)
        if y < N - 1 and x < N - 1 and \
                space[y + 1][x + 1] == EMPTY and space[y + 1][x] == EMPTY and space[y][x + 1] == EMPTY:
            dfs(y + 1, x + 1, BR)

    N = int(sys.stdin.readline())
    space = []

    res = 0

    for _ in range(N):
        space.append(list(map(int, sys.stdin.readline().split())))

    if not space[N - 1][N - 1]:
        dfs(0, 1, R)

    print(res)
