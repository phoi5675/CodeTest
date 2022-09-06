from typing import *
from sys import stdin
from collections import deque

BEER_BOX_SIZE = 20
WALK_LIMIT = 50
WALKABLE_DIST = BEER_BOX_SIZE * WALK_LIMIT

if __name__ == '__main__':
    def solve(_queue: Deque[int]) -> bool:
        while _queue:
            cur_edge = _queue.popleft()
            if cur_edge == dst:
                return True

            for other_pt, is_connected in enumerate(graph[cur_edge]):
                if is_connected and not visited[other_pt]:
                    visited[other_pt] = True
                    _queue.append(other_pt)

        return False

    T = int(input())

    for _ in range(T):
        n = int(stdin.readline().strip())
        graph: List[List[bool]] = [[False] * (n + 2) for _ in range(n + 2)]
        visited: List[bool] = [False] * (n + 2)
        coords: List[List[int]] = []
        start = 0
        dst = n + 1
        for _ in range(n + 2):
            coords.append(list(map(int, stdin.readline().strip().split())))

        # Make graph
        for i in range(n + 2):
            for j in range(i + 1, n + 2):
                x_dist: int = abs(coords[i][0] - coords[j][0])
                y_dist: int = abs(coords[i][1] - coords[j][1])
                if x_dist + y_dist <= WALKABLE_DIST:
                    graph[i][j] = graph[j][i] = True

        queue: Deque[int] = deque()
        for other_edge, is_connected in enumerate(graph[start]):
            if is_connected:
                queue.append(other_edge)
        visited[start] = True

        print('happy' if solve(queue) else 'sad')
