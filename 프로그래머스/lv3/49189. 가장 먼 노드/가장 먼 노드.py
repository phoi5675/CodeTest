from collections import deque


def solution(n, edge):
    answer = 0
    cur_max_dist = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for y, x in edge:
        graph[y].append(x)
        graph[x].append(y)
    
    Q = deque()
    Q.append((1, 0))
    visited[1] = True
    
    while Q:
        idx, dist = Q.popleft()
        if cur_max_dist == dist:
            answer += 1
        elif cur_max_dist < dist:
            cur_max_dist = dist
            answer = 1

        for i in graph[idx]:
            if not visited[i]:
                visited[i] = True
                Q.append((i, dist + 1))
        
    return answer