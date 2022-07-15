from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    Q = deque()
    
    for i in range(n):
        if visited[i]:
            continue
            
        visited[i] = True
        Q.append(computers[i])
        answer += 1
        while Q:
            computer = Q.popleft()

            for j in range(n):
                if not visited[j] and computer[j]:
                    Q.append(computers[j])
                    visited[j] = True     

    return answer