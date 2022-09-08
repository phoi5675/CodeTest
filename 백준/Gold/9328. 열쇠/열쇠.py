from sys import stdin
from typing import *
from collections import deque

WALL = '*'
EMPTY = '.'
DOC = '$'

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    def alpha_to_int(alpha: str) -> int:
        if alpha.isupper():
            return ord(alpha) - ord('A')
        else:
            return ord(alpha) - ord('a')

    def bfs() -> int:
        docs = 0
        while entrance_queue:
            y, x = entrance_queue.popleft()

            if building[y][x] == DOC:
                docs += 1
                building[y][x] = EMPTY

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if not 0 <= ny < h or not 0 <= nx < w or visited[ny][nx] or building[ny][nx] == WALL:
                    continue

                visited[ny][nx] = True
                if building[ny][nx].isupper():
                    idx = alpha_to_int(building[ny][nx])
                    if keys[idx]:
                        entrance_queue.append((ny, nx))
                    else:
                        door_queue[idx].append((ny, nx))
                elif building[ny][nx].islower():
                    idx = alpha_to_int(building[ny][nx])
                    keys[idx] = True
                    entrance_queue.append((ny, nx))
                    while door_queue[idx]:
                        entrance_queue.append((door_queue[idx].popleft()))
                else:
                    entrance_queue.append((ny, nx))

        return docs

    T = int(input())

    for _ in range(T):
        h, w = map(int, stdin.readline().strip().split())
        building: List[List[str]] = []
        keys: List[bool] = [False] * (alpha_to_int('z') + 1)
        entrance_queue: Deque[Tuple[int, int]] = deque()
        door_queue: List[Deque[Tuple[int, int]]] = [deque() for _ in range(alpha_to_int('z') + 1)]
        visited: List[List[int]] = [[0] * w for _ in range(h)]

        # Building
        for _ in range(h):
            building.append(list(stdin.readline().strip()))

        # Keys
        alpha_keys: List[str] = list(stdin.readline().strip())

        for key in alpha_keys:
            if key.isalpha():
                keys[alpha_to_int(key)] = True

        # Enqueue entrance point
        for i in range(h):
            for j in range(w):
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    if building[i][j] == DOC or building[i][j] == EMPTY:
                        entrance_queue.append((i, j))
                        visited[i][j] = True
                    elif building[i][j].islower():
                        keys[alpha_to_int(building[i][j])] = True
                        entrance_queue.append((i, j))
                        visited[i][j] = True
                    elif building[i][j].isupper():
                        door_queue[alpha_to_int(building[i][j])].append((i, j))

        # Enqueue doors
        for idx, _door_queue in enumerate(door_queue):
            if keys[idx]:
                while _door_queue:
                    i, j = _door_queue.popleft()
                    entrance_queue.append((i, j))
                    visited[i][j] = True

        print(bfs())
