from typing import *
from collections import *
from copy import deepcopy

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

EMPTY, CHEESE = 0, 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    plate: List[List[int]] = []
    visited: List[List[bool]] = [[False] * m for _ in range(n)]
    cheese_left = 0
    melt = 0
    elapsed = 0
    Q: Deque[Tuple[int, int]] = deque()
    next_queue: Deque[Tuple[int, int]] = deque()

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j]:
                cheese_left += 1
            if i == 0 or j == 0 or i == n - 1 or j == m - 1 and line[j] == EMPTY:
                Q.append((i, j))
                visited[i][j] = True

        plate.append(line)

    while cheese_left - melt > 0:
        cheese_left -= melt
        melt = 0

        while Q:
            y, x = Q.popleft()
            if plate[y][x] == CHEESE:
                melt += 1
                plate[y][x] = EMPTY

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if plate[ny][nx] == CHEESE:
                        next_queue.append((ny, nx))
                    else:
                        Q.append((ny, nx))

        Q = deepcopy(next_queue)
        next_queue.clear()
        elapsed += 1
    
    print(elapsed - 1, cheese_left, sep='\n')
