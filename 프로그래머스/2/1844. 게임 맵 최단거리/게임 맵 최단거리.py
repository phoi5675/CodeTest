from typing import *
from collections import deque

VEC = ((1, 0), (-1, 0), (0, 1), (0, -1))
EMPTY = 1

def solution(maps):
    MAP_H = len(maps)
    MAP_W = len(maps[0])
    
    DST_Y, DST_X = MAP_H - 1, MAP_W - 1
    
    answer = -1
    queue: Deque[int, int, int] = deque()
    visited: List[List[bool]] = [[False] * MAP_W for _ in range(MAP_H)]
    
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    while len(queue):
        y, x, moved = queue.popleft()
        
        # 종료조건
        if y == DST_Y and x == DST_X:
            answer = moved
            break
    
        for dy, dx in VEC:
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < MAP_H and 0 <= nx < MAP_W and \
                maps[ny][nx] == EMPTY and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, moved + 1))
            
    return answer