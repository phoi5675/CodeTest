import sys
from collections import deque

countries = []
united_countries_identifier = False

if __name__ == "__main__":
    def is_union_able(src: list, dst: list) -> bool:
        src_y, src_x = src
        dst_y, dst_x = dst

        if l <= abs(countries[src_y][src_x] - countries[dst_y][dst_x]) <= r and \
                not visited[dst_y][dst_x]:
            return True
        else:
            return False


    def make_union_bfs(cur_pos: list) -> None:
        global united_countries_identifier
        Q: deque = deque()
        Q.append(cur_pos)
        united.append(cur_pos)

        # dfs order : top, left, bottom, right (CCW)
        while len(Q):
            y, x = Q.popleft()
            visited[y][x] = True
            # top
            if 0 < y and is_union_able([y, x], [y - 1, x]):
                Q.append([y - 1, x])
                united.append([y - 1, x])
                visited[y - 1][x] = True
            # left
            if 0 < x and is_union_able([y, x], [y, x - 1]):
                Q.append([y, x - 1])
                united.append([y, x - 1])
                visited[y][x - 1] = True
            # bottom
            if y < n - 1 and is_union_able([y, x], [y + 1, x]):
                Q.append([y + 1, x])
                united.append([y + 1, x])
                visited[y + 1][x] = True
            # right
            if x < n - 1 and is_union_able([y, x], [y, x + 1]):
                Q.append([y, x + 1])
                united.append([y, x + 1])
                visited[y][x + 1] = True

        # after traverse( == # of united > 1), make population of united countries even
        if len(united) > 1:
            united_countries_identifier = True
            # add all level
            population_sum = 0
            for [_y, _x] in united:
                population_sum += countries[_y][_x]
            averaged_population = int(population_sum / len(united))

            for [_y, _x] in united:
                countries[_y][_x] = averaged_population

    n, l, r = list(map(int, sys.stdin.readline().split()))

    elapsed_days: int = 0
    for i in range(n):
        countries.append(list(map(int, sys.stdin.readline().split())))

    while True:
        visited = [[False] * n for i in range(n)]
        united_countries_identifier = False

        # check if this country has been united at this day
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    # make union for adjacent countries
                    united = []
                    make_union_bfs([i, j])

        if not united_countries_identifier:
            break
        elapsed_days += 1

    print(elapsed_days)
