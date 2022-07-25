import sys
from collections import deque
from typing import *
from copy import deepcopy

VEC = ((-1, 0), (1, 0), (0, -1), (0, 1))
INF = int(1e9)


class Node:
    def __init__(self, y: int, x: int, count: int, keys: int):
        self.y: int = y
        self.x: int = x
        self.count = count
        self.keys: int = keys

    def __str__(self):
        return f'y: {self.y}, x: {self.x}, count: {self.count}, keys: {self.keys}'


if __name__ == '__main__':
    Q: deque[Node] = deque()
    bufQ: deque[Node] = deque()
    res: int = INF
    N, M = list(map(int, input().split()))
    maze: List[List[str]] = []
    visited: List[List[List[bool]]] = [[[False] * M for _ in range(N)] for _ in range(0b111_111 + 1)]
    for i in range(N):
        line = list(sys.stdin.readline())
        line.pop()

        for j in range(M):
            if line[j] == '0':
                line[j] = '.'
                Q.append(Node(i, j, 0, 0))
        maze.append(line)

    while Q:
        node = Q.popleft()

        if node.count < res:
            for dy, dx in VEC:
                ny, nx = dy + node.y, dx + node.x
                if 0 <= ny < N and 0 <= nx < M and not visited[node.keys][ny][nx] and not maze[ny][nx] == '#':
                    visited[node.keys][ny][nx] = True
                    if maze[ny][nx] == '.' \
                            or (maze[ny][nx].isupper() and node.keys & (1 << (ord(maze[ny][nx]) - ord('A'))) != 0):
                        Q.append(Node(ny, nx, node.count + 1, node.keys))

                    elif maze[ny][nx].islower():
                        key = 1 << (ord(maze[ny][nx]) - ord('a'))
                        Q.append(Node(ny, nx, node.count + 1, node.keys | key))

                    elif maze[ny][nx].isnumeric() and int(maze[ny][nx]) == 1:
                        res = min(res, node.count + 1)

    print(-1 if res == INF else res)
