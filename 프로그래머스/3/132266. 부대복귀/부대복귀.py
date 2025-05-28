from typing import *
from collections import deque, defaultdict

def solution(n: int, roads: List[List[int]], sources: List[int], destination: int):
    answer = []
    q: Deque[Tuple[int, int]] = deque()
    visited: List[bool] = [False] * (n + 1)
    dist: List[int] = [-1] * (n + 1)
    graph: DefaultDict[int, List[int]] = defaultdict(list)
    
    for (src, dst) in roads:
        graph[src].append(dst)
        graph[dst].append(src)
        
    dist[destination] = 0
    q.append((destination, 0))
    visited[destination] = True
    
    while q:
        cur, length = q.popleft()
        
        for edge in graph[cur]:
            if not visited[edge]:
                q.append((edge, length + 1))
                dist[edge] = length + 1
                visited[edge] = True
    for src in sources:
        answer.append(dist[src])
    
    return answer
