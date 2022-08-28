from typing import *
from collections import deque

if __name__ == '__main__':
    n = int(input())
    start, dest = map(int, input().split())

    # Make 0-index
    start += -1
    dest += -1

    visited: List[bool] = [False] * n
    graph: List[List[bool]] = [[False] * n for _ in range(n)]
    Q: Deque[Tuple[int, int]] = deque()

    for _ in range(int(input())):
        a, b = map(int, input().split())
        a += -1
        b += -1

        graph[a][b] = graph[b][a] = True

    visited[start] = True
    for idx, edge in enumerate(graph[start]):
        if edge:
            Q.append((idx, 1))
            visited[idx] = True

    while Q:
        e_to, vertexes = Q.popleft()

        if e_to == dest:
            print(vertexes)
            exit(0)

        for idx, edge in enumerate(graph[e_to]):
            if not visited[idx] and edge:
                visited[idx] = True
                Q.append((idx, vertexes + 1))

    print(-1)
