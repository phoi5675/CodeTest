from typing import *
from sys import stdin

if __name__ == '__main__':
    n, m = map(int, stdin.readline().split())
    board: List[int] = []
    dice: List[int] = []
    pos = 0

    for _ in range(n):
        board.append(int(stdin.readline().strip()))

    for _ in range(m):
        dice.append(int(stdin.readline().strip()))

    for idx, moves in enumerate(dice):
        pos += moves
        if pos >= n - 1:
            print(idx + 1)
            exit(0)
        pos += board[pos]
        if pos >= n - 1:
            print(idx + 1)
            exit(0)
