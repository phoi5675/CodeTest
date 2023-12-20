MAP_SIZE = 10
PAPER_LIMIT = 5
INF = 1e9

if __name__ == '__main__':
    def find_maskable(paper_size: int, y: int, x: int) -> bool:
        for i in range(y, y + paper_size):
            for j in range(x, x + paper_size):
                if space[i][j] == 0:
                    return False
        return True

    def mask(paper_size: int, y: int, x: int, mask_to: int) -> None:
        for i in range(y, y + paper_size):
            for j in range(x, x + paper_size):
                space[i][j] = mask_to

    def dfs(y: int, x: int, count: int) -> None:
        global res
        if count > res:
            return
        if y == MAP_SIZE:
            res = min(count, res)
            return
        if x == MAP_SIZE:
            dfs(y + 1, 0, count)
            return
        if space[y][x] == 0:
            dfs(y, x + 1, count)

        for paper in range(5, 1 - 1, -1):
            if y + paper > MAP_SIZE or x + paper > MAP_SIZE or papers[paper] == 0:
                continue

            found = find_maskable(paper, y, x)
            if not found:
                continue
            mask(paper, y, x, 0)
            papers[paper] -= 1
            dfs(y, x + paper, count + 1)
            mask(paper, y, x, 1)
            papers[paper] += 1

    space = []
    papers = [5] * (PAPER_LIMIT + 1)
    papers[0] = 0
    res = INF
    for _ in range(MAP_SIZE):
        space.append(list(map(int, input().split())))

    dfs(0, 0, 0)
    if res == INF:
        print(-1)
    else:
        print(res)
