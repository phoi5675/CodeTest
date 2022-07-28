from typing import *
from collections import deque
from copy import deepcopy

VEC = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
INF = int(1e9)

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    space: List[List[int]] = []
    sharks: List[Tuple[int, int]] = []
    visited: List[List[bool]] = [[False] * M for _ in range(N)]
    _visited = deepcopy(visited)
    distances: List[List[int]] = [[INF] * M for _ in range(N)]
    res: int = 0
    Q: Deque[Tuple[int, int, int]] = deque()

    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            if line[j] == 1:
                sharks.append((i, j))

        space.append(line)

    # Find safe distances for each shark using bfs
    for i, shark in enumerate(sharks):
        visited = deepcopy(_visited)
        Q.append((shark[0], shark[1], 0))
        visited[shark[0]][shark[1]] = True

        while Q:
            y, x, dist = Q.popleft()

            # Find minimum value
            distances[y][x] = min(distances[y][x], dist)

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    visited[ny][nx] = True
                    Q.append((ny, nx, dist + 1))

    for line in distances:
        res = max(res, max(line))
    print(res)
