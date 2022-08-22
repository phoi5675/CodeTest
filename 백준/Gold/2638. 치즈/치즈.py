from typing import *
from collections import deque

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
EMPTY, CHEESE = 0, 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    paper: List[List[int]] = []
    search_queue: Deque[Tuple[int, int]] = deque()
    melt_queue: Deque[Tuple[int, int]] = deque()
    visited: List[List[int]] = [[0] * m for _ in range(n)]
    cheese_left = 0
    elapsed = 0

    for i in range(n):
        line: List[int] = list(map(int, input().split()))
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                search_queue.append((i, j))
                visited[i][j] = 1
            if line[j]:
                cheese_left += 1
        paper.append(line)

    while cheese_left:
        while search_queue:
            y, x = search_queue.popleft()

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if not visited[ny][nx]:
                        visited[ny][nx] += 1
                        if paper[ny][nx] == EMPTY:
                            search_queue.append((ny, nx))
                    elif visited[ny][nx] == 1 and paper[ny][nx] == CHEESE:
                        visited[ny][nx] = 2
                        melt_queue.append((ny, nx))

        while melt_queue:
            y, x = melt_queue.popleft()
            paper[y][x] = EMPTY
            cheese_left -= 1

            search_queue.append((y, x))
            visited[y][x] = 1

        elapsed += 1

    print(elapsed)
