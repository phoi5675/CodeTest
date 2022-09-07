from sys import stdin
from typing import *
from collections import deque

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
NOT_VISITED, WAND, BROKEN = 0b00, 0b01, 0b10
EMPTY, WALL = 0, 1

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    h_y, h_x = map(int, stdin.readline().strip().split())
    e_y, e_x = map(int, stdin.readline().strip().split())
    h_y -= 1
    h_x -= 1
    e_y -= 1
    e_x -= 1
    arr: List[List[int]] = []
    visited: List[List[int]] = [[NOT_VISITED] * m for _ in range(n)]
    queue: Deque[Tuple[int, int, int, bool]] = deque()

    queue.append((h_y, h_x, 0, False))
    visited[h_y][h_x] = WAND

    for _ in range(n):
        arr.append(list(map(int, stdin.readline().strip().split())))

    while queue:
        y, x, moves, is_wand_used = queue.popleft()

        if y == e_y and x == e_x:
            print(moves)
            exit(0)

        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if not is_wand_used and visited[ny][nx] & WAND == NOT_VISITED:
                    visited[ny][nx] |= WAND
                    if arr[ny][nx] == EMPTY:
                        queue.append((ny, nx, moves + 1, is_wand_used))
                    elif arr[ny][nx] == WALL:
                        queue.append((ny, nx, moves + 1, not is_wand_used))
                elif is_wand_used and visited[ny][nx] & BROKEN == NOT_VISITED and arr[ny][nx] == EMPTY:
                    visited[ny][nx] |= BROKEN
                    queue.append((ny, nx, moves + 1, is_wand_used))

    print(-1)
