import sys
from typing import *
sys.setrecursionlimit(20_000)

EMPTY, WALL, PIPE = '.', 'x', '0'

VEC = ((-1, 1), (0, 1), (1, 1))

deployed_pipes = 0

if __name__ == '__main__':
    def dfs(y: int, x: int) -> bool:
        if x == c - 1:
            return True

        for dy, dx in VEC:
            ny, nx = y + dy, x + dx

            if 0 <= ny < r and 0 <= nx < c and field[ny][nx] == EMPTY:
                field[ny][nx] = PIPE
                if dfs(ny, nx):
                    return True

        return False


    r, c = map(int, input().split())
    field: List[List[str]] = []

    for _ in range(r):
        field.append(list(sys.stdin.readline().strip()))

    for row in range(r):
        if field[row][0] == EMPTY:
            field[row][0] = PIPE
            if dfs(row, 0):
                deployed_pipes += 1

    print(deployed_pipes)
