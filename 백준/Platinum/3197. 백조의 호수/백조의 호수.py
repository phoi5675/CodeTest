import sys
from collections import deque
from copy import deepcopy
from typing import *

VEC = ((-1, 0), (1, 0), (0, -1), (0, 1))
LAKE, ICE = '.', 'X'

if __name__ == '__main__':
    def bfs_ice(Q: deque) -> deque:
        bufQ = deque()
        while Q:
            y, x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = dy + y, dx + x
                if 0 <= ny < R and 0 <= nx < C and lake[ny][nx] == ICE:
                    bufQ.append((ny, nx))
                    lake[ny][nx] = LAKE
        return bufQ


    def is_swan_reachable(Q: deque) -> (bool, deque):
        reachable = False
        bufQ = deque()
        while Q and not reachable:
            y, x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = dy + y, dx + x
                if 0 <= ny < R and 0 <= nx < C:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        # 호수인 지역은 오늘 탐색 가능하므로 현재 탐색 진행중인 Q에 삽입
                        if lake[ny][nx] == LAKE:
                            Q.append((ny, nx))
                        # 빙판인 지역은 오늘 얼음이 녹은 이후에 탐색 가능하므로 내일 탐색할 Q에 삽입
                        elif lake[ny][nx] == ICE:
                            bufQ.append((ny, nx))
                    if ny == s2[0] and nx == s2[1]:
                        reachable = True
                        break
        return reachable, bufQ


    R, C = list(map(int, input().split()))
    visited: List[List[bool]] = [[False] * C for _ in range(R)]

    elapsed: int = 0
    lake: List[List[str]] = []
    s1: List[int] = []
    s2: List[int] = []
    bufferQ = deque()
    buf_moveQ = deque()
    is_reachable: bool = False

    swanQ, waterQ = deque(), deque()
    for i in range(R):
        line = list(sys.stdin.readline())
        line.pop()
        for j in range(C):
            if line[j] == 'L':
                if not s1:
                    s1 = [i, j]
                    line[j] = LAKE
                elif not s2:
                    s2 = [i, j]
                    line[j] = LAKE
            if line[j] == '.':
                # 첫날은 모든 호수에 대해서 얼음이 인접했는지 확인해야 하므로 모든 물에 대해서 탐색
                bufferQ.append((i, j))
        lake.append(line)

    buf_moveQ.append(s1)
    visited[s1[0]][s1[1]] = True

    while not is_reachable:
        # Calculate when swans can meet
        swanQ = buf_moveQ
        is_reachable, buf_moveQ = is_swan_reachable(swanQ)
        if is_reachable:
            break
        # Melt ice
        waterQ = bufferQ
        bufferQ = bfs_ice(waterQ)

        elapsed += 1

    print(elapsed)
