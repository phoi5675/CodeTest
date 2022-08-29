from typing import *
from collections import deque

SEA, ISLAND, VISITED = 0, 1, -1

VEC = ((-1, -1), (-1, 0), (-1, 1),
       (0, -1), (0, 1),
       (1, -1), (1, 0), (1, 1))

if __name__ == '__main__':
    def bfs(y: int, x: int) -> None:
        Q: Deque[Tuple[int, int]] = deque()
        Q.append((y, x))
        world[y][x] = VISITED

        while Q:
            cur_y, cur_x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = cur_y + dy, cur_x + dx
                if 0 <= ny < h and 0 <= nx < w and world[ny][nx] == ISLAND:
                    world[ny][nx] = VISITED
                    Q.append((ny, nx))

        return

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        num_of_islands = 0
        world: List[List[int]] = []

        for _ in range(h):
            world.append(list(map(int, input().split())))

        for i in range(h):
            for j in range(w):
                if world[i][j] == ISLAND:
                    bfs(i, j)
                    num_of_islands += 1

        print(num_of_islands)
