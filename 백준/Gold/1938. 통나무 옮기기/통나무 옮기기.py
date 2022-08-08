from typing import *
from collections import deque

LOG_LEN = 3
VEC = ((1, 0), (-1, 0), (0, 1), (0, -1))
BOUNDARY = (((1, 0), (-1, 0)), ((0, 1), (0, -1)))
TURN_BOUNDARY = (((-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)),
                 ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)))
VERT, HOR = 0, 1

if __name__ == '__main__':
    def is_horizontal(log_pos: List[Tuple[int, int]]) -> int:
        return log_pos[0][0] == log_pos[1][0] == log_pos[2][0]


    def is_placeable(_y: int, _x: int, _is_horizontal: int, boundary: List) -> bool:
        for _dy, _dx in boundary:
            _ny, _nx = _y + _dy, _x + _dx
            if (0 <= _ny < n and 0 <= _nx < n and field[_ny][_nx] == 1) or \
                    not 0 <= _ny < n or not 0 <= _nx < n:
                return False
        return True


    def get_center(log_pos: List[Tuple[int, int]]) -> tuple:
        return sum(pos[0] for pos in log_pos) // 3, sum(pos[1] for pos in log_pos) // 3


    n = int(input())
    field: List[List[int]] = []
    start_log: List[Tuple[int, int]] = []
    dst_log: List[Tuple[int, int]] = []
    start_info: List[int] = []
    dst_info: List[int] = []
    visited: List[List[List[bool]]] = [[[False] * n for _ in range(n)] for _ in range(2)]
    Q: Deque = deque()

    for i in range(n):
        line = list(input())
        for j in range(n):
            if line[j] == 'B':
                start_log.append((i, j))
                line[j] = '0'
            elif line[j] == 'E':
                dst_log.append((i, j))
                line[j] = '0'
        field.append(list(map(int, line)))

    start_info.extend(get_center(start_log))
    start_info.append(is_horizontal(start_log))
    dst_info.extend(get_center(dst_log))
    dst_info.append(is_horizontal(dst_log))

    visited[start_info[2]][start_info[0]][start_info[1]] = True
    Q.append((*start_info, 0))

    while Q:
        y, x, horizontal, moves = Q.popleft()

        if y == dst_info[0] and x == dst_info[1] and horizontal == dst_info[2]:
            print(moves)
            exit(0)

        # Move log
        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[horizontal][ny][nx] and field[ny][nx] != 1 \
                    and is_placeable(ny, nx, horizontal, BOUNDARY[horizontal]):
                visited[horizontal][ny][nx] = True
                Q.append((ny, nx, horizontal, moves + 1))

        # Turn log
        turned: int = not horizontal
        if not visited[turned][y][x] and is_placeable(y, x, turned, TURN_BOUNDARY[horizontal]):
            visited[turned][y][x] = True
            Q.append((y, x, turned, moves + 1))

    print(0)
