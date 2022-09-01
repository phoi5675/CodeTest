from sys import stdin
from typing import *
from collections import deque

VEC = ((1, 0, 0), (-1, 0, 0),
       (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

EMPTY, NOT_RIPEN, RIPEN = -1, 0, 1

if __name__ == '__main__':
    m, n, h = map(int, input().split())
    boxes: List[List[List[int]]] = []
    elapsed = 0
    not_ripen_tomatoes = 0
    queue: Deque[Tuple[int, int, int]] = deque()
    next_queue: Deque[Tuple[int, int, int]] = deque()

    for i in range(h):
        box: List[List[int]] = []
        for j in range(n):
            line: List[int] = list(map(int, stdin.readline().split()))
            for k in range(m):
                if line[k] == NOT_RIPEN:
                    not_ripen_tomatoes += 1
                elif line[k] == RIPEN:
                    queue.append((i, j, k))
            box.append(line)
        boxes.append(box)

    while queue:
        if not_ripen_tomatoes == 0:
            break
            
        while queue:
            z, y, x = queue.popleft()

            for dz, dy, dx in VEC:
                nz, ny, nx = z + dz, y + dy, x + dx
                if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and boxes[nz][ny][nx] == NOT_RIPEN:
                    boxes[nz][ny][nx] = RIPEN
                    not_ripen_tomatoes -= 1
                    next_queue.append((nz, ny, nx))

        while next_queue:
            queue.append(next_queue.popleft())

        elapsed += 1

    print(elapsed if not_ripen_tomatoes == 0 else -1)
