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
                    if not swan_visited[ny][nx]:
                        swan_visited[ny][nx] = True
                        if lake[ny][nx] != ICE:
                            Q.append((ny, nx))
                        elif lake[ny][nx] == ICE:
                            bufQ.append((ny, nx))
                    if ny == s2[0] and nx == s2[1]:
                        reachable = True
        return reachable, bufQ


    R, C = list(map(int, input().split()))
    visited: List[List[bool]] = [[False] * C for _ in range(R)]

    elapsed: int = 0
    swan_visited = deepcopy(visited)
    ice_visited = deepcopy(visited)
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
                bufferQ.append((i, j))
        lake.append(line)

    buf_moveQ.append(s1)
    swan_visited[s1[0]][s1[1]] = True

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
