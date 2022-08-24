from typing import *
from collections import deque
from copy import deepcopy

ROCK = 'X'
EMPTY = '.'
WATER = '*'
CAVE = 'D'
HOG = 'S'

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    r, c = map(int, input().split())

    visited: List[List[bool]] = [[False] * c for _ in range(r)]
    water_queue: Deque[Tuple[int, int]] = deque()
    hog_queue: Deque[Tuple[int, int, int]] = deque()
    forest: List[List[str]] = []

    for i in range(r):
        line = list(input())
        for j in range(c):
            if line[j] == WATER:
                water_queue.append((i, j))
            elif line[j] == HOG:
                visited[i][j] = True
                hog_queue.append((i, j, 0))
        forest.append(line)

    next_water_queue = deque()
    next_hog_queue = deque()

    while hog_queue:
        while water_queue:
            y, x = water_queue.popleft()

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < r and 0 <= nx < c and forest[ny][nx] == EMPTY:
                    next_water_queue.append((ny, nx))
                    forest[ny][nx] = WATER
        water_queue = deepcopy(next_water_queue)
        next_water_queue.clear()

        while hog_queue:
            y, x, elapsed = hog_queue.popleft()

            if forest[y][x] == CAVE:
                print(elapsed)
                exit(0)

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and \
                        (forest[ny][nx] == EMPTY or forest[ny][nx] == CAVE):
                    visited[ny][nx] = True
                    next_hog_queue.append((ny, nx, elapsed + 1))

        hog_queue = deepcopy(next_hog_queue)
        next_hog_queue.clear()

    print("KAKTUS")
