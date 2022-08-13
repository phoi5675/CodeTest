from typing import *
from collections import deque

BOARD_SIZE = 5
DIGIT_LEN = 6
VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

generated_nums = 0


def bfs(i: int, j: int) -> None:
    global generated_nums
    Q = deque()
    Q.append((i, j, 1, space[i][j]))

    while Q:
        y, x, digits, cur_num = Q.popleft()

        if digits == DIGIT_LEN:
            if not numbers_visited[cur_num]:
                numbers_visited[cur_num] = True
                generated_nums += 1
            continue

        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < BOARD_SIZE and 0 <= nx < BOARD_SIZE:
                Q.append((ny, nx, digits + 1, cur_num * 10 + space[ny][nx]))


if __name__ == '__main__':
    space: List[List[int]] = []
    numbers_visited: List[bool] = [False] * 1_000_000

    for _ in range(BOARD_SIZE):
        space.append(list(map(int, input().split())))

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            bfs(i, j)

    print(generated_nums)
