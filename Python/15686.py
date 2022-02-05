import sys


if __name__ == "__main__":
    def calc_chicken_distances(_chicken: list, _homes: list) -> int:
        dist = 0
        for h in _homes:
            home_to_chicken = sys.maxsize
            for ch in _chicken:
                h_y, h_x = h
                ch_y, ch_x = ch
                home_to_chicken = min(home_to_chicken, abs(ch_y - h_y) + abs(ch_x - h_x))
            dist += home_to_chicken

        return dist

    def dfs(survived_chickens: list, index: int, depth: int, depth_limit: int) -> None:
        global city_chicken_distance
        if depth == depth_limit:
            city_chicken_distance = min(city_chicken_distance, calc_chicken_distances(survived_chickens, homes))
            return

        for i in range(index, len(chickens)):
            survived_chickens.append(chickens[i])
            dfs(survived_chickens[:], i + 1, depth + 1, depth_limit)
            survived_chickens.pop()

    HOME, CHICKEN = 1, 2
    n, m = list(map(int, sys.stdin.readline().split()))
    city = []
    homes = []
    chickens = []
    city_chicken_distance = sys.maxsize

    for i in range(n):
        city.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(n):
            if city[i][j] == HOME:
                homes.append((i, j))
            elif city[i][j] == CHICKEN:
                chickens.append((i, j))

    # traverse
    dfs([], 0, 0, m)

    print(city_chicken_distance)
