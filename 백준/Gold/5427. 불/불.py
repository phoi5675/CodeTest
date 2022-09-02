from sys import stdin
from typing import *
from collections import deque
from copy import deepcopy

EMPTY, WALL, SANG, FIRE = '.', '#', '@', '*'

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    def solve() -> int:
        w, h = map(int, input().split())
        building: List[List[str]] = []
        fire_queue: Deque[Tuple[int, int]] = deque()
        next_fire_queue: Deque[Tuple[int, int]] = deque()
        sang_queue: Deque[Tuple[int, int]] = deque()
        next_sang_queue: Deque[Tuple[int, int]] = deque()
        visited: List[List[bool]] = [[False] * w for _ in range(h)]
        elapsed = 0

        for i in range(h):
            line = list(stdin.readline().strip())
            for j in range(w):
                if line[j] == SANG:
                    line[j] = EMPTY
                    sang_queue.append((i, j))
                    visited[i][j] = True
                elif line[j] == FIRE:
                    fire_queue.append((i, j))
            building.append(line)

        while fire_queue or sang_queue:
            while fire_queue:
                y, x = fire_queue.popleft()

                for dy, dx in VEC:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and building[ny][nx] == EMPTY:
                        building[ny][nx] = FIRE
                        next_fire_queue.append((ny, nx))

            while sang_queue:
                y, x = sang_queue.popleft()

                if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                    return elapsed + 1

                for dy, dx in VEC:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and building[ny][nx] == EMPTY and not visited[ny][nx]:
                        visited[ny][nx] = True
                        next_sang_queue.append((ny, nx))

            fire_queue = deepcopy(next_fire_queue)
            next_fire_queue.clear()
            sang_queue = deepcopy(next_sang_queue)
            next_sang_queue.clear()

            elapsed += 1

        return 0

    n = int(input())

    for _ in range(n):
        ans = solve()
        print(ans if ans else "IMPOSSIBLE")
