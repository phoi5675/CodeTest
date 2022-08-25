from typing import *

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
VERT = ((-1, 0), (1, 0))
HORI = ((0, 1), (0, -1))

edible_candies = 0

if __name__ == '__main__':
    def count_candies(y: int, x: int, dy: int, dx: int) -> int:
        same_candies = 0
        ny, nx = y + dy, x + dx
        while 0 <= ny < n and 0 <= nx < n and bomboni[y][x] == bomboni[ny][nx]:
            same_candies += 1
            ny += dy
            nx += dx

        return same_candies

    n = int(input())
    bomboni: List[List[str]] = []

    for _ in range(n):
        bomboni.append(list(input()))

    for i in range(n):
        for j in range(n):
            vert_candies = 1
            hori_candies = 1
            for (vdy, vdx), (hdy, hdx) in zip(VERT, HORI):
                vert_candies += count_candies(i, j, vdy, vdx)
                hori_candies += count_candies(i, j, hdy, hdx)

            edible_candies = max(edible_candies, vert_candies, hori_candies)

            for dy, dx in VEC:
                vert_candies = 1
                hori_candies = 1
                ny, nx = i + dy, j + dx
                if 0 <= ny < n and 0 <= nx < n and bomboni[i][j] != bomboni[ny][nx]:
                    bomboni[i][j], bomboni[ny][nx] = bomboni[ny][nx], bomboni[i][j]
                    for (vdy, vdx), (hdy, hdx) in zip(VERT, HORI):
                        vert_candies += count_candies(i, j, vdy, vdx)
                        hori_candies += count_candies(i, j, hdy, hdx)
                    bomboni[i][j], bomboni[ny][nx] = bomboni[ny][nx], bomboni[i][j]
                edible_candies = max(edible_candies, vert_candies, hori_candies)

    print(edible_candies)
