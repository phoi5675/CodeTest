from sys import stdin
from collections import deque
from typing import *

EMPTY, NOT_RIPEN, RIPEN = -1, 0, 1

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    def bfs(_queue: Deque[Tuple[int, int]], tomatoes_left: int) -> Tuple[Deque[Tuple[int, int]], int]:
        next_queue: Deque[Tuple[int, int]] = deque()
        while _queue:
            y, x = _queue.popleft()

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and boxes[ny][nx] == NOT_RIPEN:
                    boxes[ny][nx] = RIPEN
                    next_queue.append((ny, nx))
                    tomatoes_left -= 1

        return next_queue, tomatoes_left

    m, n = map(int, input().split())
    not_ripen_tomatoes = 0
    elapsed = 0
    boxes: List[List[int]] = []
    queue: Deque[Tuple[int, int]] = deque()

    for i in range(n):
        line = list(map(int, stdin.readline().strip().split()))
        for j in range(m):
            if line[j] == NOT_RIPEN:
                not_ripen_tomatoes += 1
            elif line[j] == RIPEN:
                queue.append((i, j))
        boxes.append(line)

    while queue and not_ripen_tomatoes > 0:
        queue, not_ripen_tomatoes = bfs(queue, not_ripen_tomatoes)
        elapsed += 1

    print(-1 if not_ripen_tomatoes else elapsed)
