from typing import *
from collections import deque


MAP_SIZE = 101 + 1  # 겹친 직사각형 테두리 탐색을 위해 직사각형 표시한 지도에 공백 추가
VECT = ((-1, 0), (1, 0), (0, 1), (0, -1))
CORNERS = ((-1, -1), (-1, 1), (1, -1), (1, 1))  # 경로 지도 생성 시 모서리 부분 누락 방지


def find_path_map(rect_map: List[List[int]]) -> List[List[int]]:
    visited: List[List[bool]] = [[False] * MAP_SIZE for _ in range(MAP_SIZE)]
    path_map: List[List[int]] = [[0] * MAP_SIZE for _ in range(MAP_SIZE)]
    q: Deque[Tuple[int, int]] = deque()
    q.append((0, 0))
    
    # (0, 0)을 시작으로, 사각형 테두리와 만나는 부분만 지도에 표시
    while q:
        y, x = q.popleft()
        
        for dy, dx in (VECT + CORNERS):
            ny, nx = dy + y, dx + x
            
            if (0 <= ny < MAP_SIZE and 0 <= nx < MAP_SIZE) and not visited[ny][nx]:
                visited[ny][nx] = True
                if rect_map[ny][nx]:
                    path_map[ny][nx] = 1
                else:
                    q.append((ny, nx))
    
    return path_map
                

def bfs(path_map: List[List[int]], c_x: int, c_y: int, i_x: int, i_y: int) -> int:
    visited: List[List[bool]] = [[False] * MAP_SIZE for _ in range(MAP_SIZE)]
    q: Deque[Tuple[int, int, int]] = deque()
    q.append((c_y, c_x, 0))
    
    while q:
        y, x, moved = q.popleft()

        if y == i_y and x == i_x:
            return moved
        
        for dy, dx in VECT:
            ny, nx = dy + y, dx + x
            
            if (0 <= ny < MAP_SIZE and 0 <= nx < MAP_SIZE) and \
                    not visited[ny][nx] and path_map[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, moved + 1))
    
    return -1
    
    
def solution(rectangle: List[List[int]], characterX: int, characterY: int, itemX: int, itemY: int) -> int:
    rect_map: List[List[int]] = [[0] * (MAP_SIZE) for _ in range(MAP_SIZE)]
    
    # 좌표 2배 업스케일
    for i in range(len(rectangle)):
        for j in range(len(rectangle[i])):
            rectangle[i][j] *= 2
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    # 사각형 겹치는 부분을 지도에 생성
    for idx, (start_x, start_y, end_x, end_y) in enumerate(rectangle):
        for i in range(start_y, end_y + 1):
            for j in range(start_x, end_x + 1):
                rect_map[i][j] = 1
                
    # 겹친 사각형에서 길 지도 생성
    path_map = find_path_map(rect_map)
            
    answer = bfs(path_map, characterX, characterY, itemX, itemY) // 2
    return answer
