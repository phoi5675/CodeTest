from typing import *
from collections import deque
from copy import deepcopy

EMPTY, WALL = '.', '#'

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    r, c = map(int, input().split())
    maze: List[List[str]] = []
    init_jihun: List[int] = []
    visited: List[List[bool]] = [[False] * c for _ in range(r)]

    fire_queue: Deque[Tuple[int, int]] = deque()
    jihun_queue: Deque[Tuple[int, int, int]] = deque()
    next_fire_queue: Deque[Tuple[int, int]] = deque()
    next_jihun_queue: Deque[Tuple[int, int, int]] = deque()

    for i in range(r):
        line = list(input())
        for j in range(c):
            if line[j] == 'J':
                visited[i][j] = True
                line[j] = EMPTY
                jihun_queue.append((i, j, 0))
            elif line[j] == 'F':
                fire_queue.append((i, j))
        maze.append(line)

    while jihun_queue or fire_queue:
        while jihun_queue:
            y, x, elapsed = jihun_queue.popleft()

            if maze[y][x] == EMPTY and (y == 0 or y == r - 1 or x == 0 or x == c - 1):
                print(elapsed + 1)
                exit(0)
            elif maze[y][x] == 'F':
                continue

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and maze[ny][nx] == EMPTY:
                    visited[ny][nx] = True
                    next_jihun_queue.append((ny, nx, elapsed + 1))

        while fire_queue:
            y, x = fire_queue.popleft()

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < r and 0 <= nx < c and maze[ny][nx] == EMPTY:
                    maze[ny][nx] = 'F'
                    next_fire_queue.append((ny, nx))

        fire_queue = deepcopy(next_fire_queue)
        next_fire_queue.clear()
        jihun_queue = deepcopy(next_jihun_queue)
        next_jihun_queue.clear()

    print("IMPOSSIBLE")
