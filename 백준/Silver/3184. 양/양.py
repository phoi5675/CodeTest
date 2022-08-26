from typing import *
from collections import deque

SHEEP, WOLF = 'o', 'v'
EMPTY, WALL = '.', '#'

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

num_of_sheep, num_of_wolves = 0, 0

if __name__ == '__main__':
    def bfs(y: int, x: int) -> None:
        global num_of_sheep, num_of_wolves
        
        visited[y][x] = True
        local_sheep, local_wolves = 0, 0
        Q: Deque[Tuple[int, int]] = deque()
        Q.append((y, x))

        while Q:
            cur_y, cur_x = Q.popleft()

            if field[cur_y][cur_x] == SHEEP:
                local_sheep += 1
            elif field[cur_y][cur_x] == WOLF:
                local_wolves += 1

            for dy, dx in VEC:
                ny, nx = cur_y + dy, cur_x + dx

                if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and field[ny][nx] != WALL:
                    visited[ny][nx] = True
                    Q.append((ny, nx))

        if local_sheep > local_wolves:
            num_of_wolves -= local_wolves
        else:
            num_of_sheep -= local_sheep

    r, c = map(int, input().split())
    visited: List[List[bool]] = [[False] * c for _ in range(r)]
    field: List[List[str]] = []

    for i in range(r):
        line = list(input())
        for j in range(c):
            if line[j] == SHEEP:
                num_of_sheep += 1
            elif line[j] == WOLF:
                num_of_wolves += 1
        field.append(line)

    for i in range(r):
        for j in range(c):
            if field[i][j] != WALL and not visited[i][j]:
                bfs(i, j)

    print(num_of_sheep, num_of_wolves, sep=' ')
