import sys
from typing import *
from collections import deque
from copy import deepcopy

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    ice_map: List[List[int]] = []
    visited: List[List[int]] = [[-1] * m for _ in range(n)]
    melt_map: List[List[int]] = [[0] * m for _ in range(n)]
    ice_queue, next_ice_queue = deque(), deque()
    tmp_queue, clustered_queue = deque(), deque()

    elapsed = 0
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(m):
            if line[j] != 0:
                ice_queue.append((i, j))
        ice_map.append(line)

    while ice_queue:
        # Cluster iceberg
        y, x = ice_queue.popleft()
        visited[y][x] = elapsed + 1
        tmp_queue.append((y, x))
        clustered_queue.append((y, x))

        while tmp_queue:
            y, x = tmp_queue.popleft()
            melt: int = 0
            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if visited[ny][nx] <= elapsed and ice_map[ny][nx] > 0:
                        visited[ny][nx] = elapsed + 1
                        tmp_queue.append((ny, nx))
                        clustered_queue.append((ny, nx))
                    elif ice_map[ny][nx] == 0:
                        melt += 1

            melt_map[y][x] = melt

        # Check cluster
        while ice_queue:
            y, x = ice_queue.popleft()

            # If an iceberg is not clustered yet, iceberg has been separated.
            if ice_map[y][x] > 0 and visited[y][x] <= elapsed:
                print(elapsed)
                exit(0)

        # Melt iceberg and enqueue
        while clustered_queue:
            y, x = clustered_queue.popleft()
            ice_map[y][x] -= melt_map[y][x]
            if ice_map[y][x] > 0:
                next_ice_queue.append((y, x))
                visited[y][x] = elapsed + 1
            else:
                ice_map[y][x] = 0

        ice_queue = deepcopy(next_ice_queue)
        next_ice_queue.clear()
        clustered_queue.clear()
        elapsed += 1

    print(0)
