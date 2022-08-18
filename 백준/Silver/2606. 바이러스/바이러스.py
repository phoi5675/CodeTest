from typing import *
from collections import deque

"""
- Use 1-based index
"""

if __name__ == '__main__':
    n = int(input())
    connected = int(input())
    graph: List[List[bool]] = [[False] * (n + 1) for _ in range(n + 1)]
    visited: List[bool] = [False] * (n + 1)
    Q: Deque[int] = deque()

    for _ in range(connected):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = True
        if a == 1:
            Q.append(b)
            visited[b] = True
        elif b == 1:
            Q.append(a)
            visited[a] = True

    while Q:
        com = Q.popleft()

        for idx, _ in enumerate(graph[com]):
            if not visited[idx] and graph[com][idx]:
                Q.append(idx)
                visited[idx] = True

    # Do not count 1st computer
    print(sum(virus for virus in visited if virus) - 1)
