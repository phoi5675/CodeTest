from sys import stdin
from typing import *
from collections import deque

VEC = ((-1, -2), (-2, -1), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1))

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        I = int(stdin.readline().strip())
        start: List[int] = list(map(int, stdin.readline().strip().split()))
        dst: List[int] = list(map(int, stdin.readline().strip().split()))
        visited: List[List[bool]] = [[False] * I for _ in range(I)]
        queue: Deque[Tuple[int, int, int]] = deque()

        queue.append((start[0], start[1], 0))

        while queue:
            y, x, elapsed = queue.popleft()

            if y == dst[0] and x == dst[1]:
                print(elapsed)
                break

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < I and 0 <= nx < I and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, elapsed + 1))
