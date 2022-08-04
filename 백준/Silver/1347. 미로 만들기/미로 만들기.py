from typing import *
from collections import deque

VEC = ((-1, 0), (0, -1), (1, 0), (0, 1))
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
MAZE_WIDTH = 100 + 1

if __name__ == '__main__':
    def change_vector(is_clockwise: bool, _vec: int) -> int:
        if is_clockwise:
            return (_vec + 3) % len(VEC)
        else:
            return (_vec + 1) % len(VEC)

    n = int(input())
    Q: Deque[Tuple[int, int]] = deque()
    vec = DOWN
    upper_left: List[int] = [0, 0]
    lower_right: List[int] = [0, 0]
    maze: List[List[str]] = [['#'] * MAZE_WIDTH for _ in range(MAZE_WIDTH)]
    commands = list(input())

    Q.append((0, 0))

    for com in commands:
        if com == 'R' or com == 'L':
            vec = change_vector(com == 'R', vec)
        elif com == 'F':
            cur_y, cur_x = Q[-1]
            ny, nx = cur_y + VEC[vec][0], cur_x + VEC[vec][1]
            Q.append((ny, nx))
            upper_left[0] = min(upper_left[0], ny)
            upper_left[1] = min(upper_left[1], nx)
            lower_right[0] = max(lower_right[0], ny)
            lower_right[1] = max(lower_right[1], nx)

    offset_y = -upper_left[0] if upper_left[0] < 0 else 0
    offset_x = -upper_left[1] if upper_left[1] < 0 else 0

    while Q:
        y, x = Q.popleft()
        maze[y + offset_y][x + offset_x] = '.'
    for i in range(upper_left[0], lower_right[0] + 1):
        for j in range(upper_left[1], lower_right[1] + 1):
            print(maze[i + offset_y][j + offset_x], end='')
        print()
