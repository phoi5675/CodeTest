from typing import *

EMPTY = 0
NOT_SAFE = 4
PAWN, KNIGHT, QUEEN = 1, 2, 3
KNIGHT_MOVES = ((-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1))
QUEEN_MOVES = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    board: List[List[int]] = [[EMPTY] * m for _ in range(n)]
    safe_area = n * m

    queen, knight, pawn = [], [], []

    for idx, unit in enumerate((queen, knight, pawn)):
        unit_input = list(map(int, input().split()))
        for i in range(1, 2 * unit_input[0], 2):
            y, x = unit_input[i] - 1, unit_input[i + 1] - 1
            unit.append((y, x))
            board[y][x] = idx + 1
            safe_area -= 1

    # move knights
    for y, x in knight:
        for dy, dx in KNIGHT_MOVES:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == EMPTY:
                board[ny][nx] = NOT_SAFE
                safe_area -= 1

    # move queens
    for y, x in queen:
        for dy, dx in QUEEN_MOVES:
            is_movable = True
            i = 1
            while is_movable:
                ny, nx = y + dy * i, x + dx * i
                if 0 <= ny < n and 0 <= nx < m:
                    if board[ny][nx] == EMPTY:
                        board[ny][nx] = NOT_SAFE
                        safe_area -= 1
                    elif board[ny][nx] == NOT_SAFE:
                        pass
                    else:
                        is_movable = False
                        break
                else:
                    is_movable = False
                    break
                i += 1

    print(safe_area)
