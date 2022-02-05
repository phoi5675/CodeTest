import sys
import copy

if __name__ == "__main__":
    def move(_board: list, vector: tuple, level: int):
        table = copy.deepcopy(_board)
        x, y = vector

        if vector == UP or vector == LEFT:
            row_start, row_end = 0, n
            col_start, col_end = 0, n
            step = 1
        else:
            row_start, row_end = n - 1, 0 - 1
            col_start, col_end = n - 1, 0 - 1
            step = -1

        for i in range(row_start, row_end, step):
            for j in range(col_start, col_end, step):
                if table[i][j] == 0:
                    continue
                # merge block
                offset_x, offset_y = -x, -y
                while x and 0 <= j + offset_x < n and table[i][j + offset_x] == 0:
                    offset_x -= x
                while y and 0 <= i + offset_y < n and table[i + offset_y][j] == 0:
                    offset_y -= y

                # merge & swap
                if 0 <= j + offset_x < n and 0 <= i + offset_y < n \
                        and table[i][j] == table[i + offset_y][j + offset_x]:
                    table[i][j], table[i + offset_y][j + offset_x] = table[i][j] + table[i + offset_y][j + offset_x], 0
                # not merged
                else:
                    offset_x, offset_y = 0, 0

                # move block
                merged_x, merged_y = j, i  # if block is merged, we should change coord
                move_x, move_y = x, y
                while move_x and 0 <= merged_x + move_x + x < n \
                        and table[merged_y + move_y][merged_x + move_x + x] == 0:
                    move_x += x
                while move_y and 0 <= merged_y + move_y + y < n \
                        and table[merged_y + move_y + y][merged_x + move_x] == 0:
                    move_y += y

                if 0 <= merged_x + move_x < n and 0 <= merged_y + move_y < n and \
                        table[merged_y + move_y][merged_x + move_x] == 0:
                    table[merged_y][merged_x], table[merged_y + move_y][merged_x + move_x] \
                        = table[merged_y + move_y][merged_x + move_x], table[merged_y][merged_x]

        # traverse
        if level < 5:
            _up = move(table, UP, level + 1)
            _down = move(table, DOWN, level + 1)
            _left = move(table, LEFT, level + 1)
            _right = move(table, RIGHT, level + 1)
        else:
            return max(map(max, table))

        return max(_up, _down, _left, _right)


    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    n = int(sys.stdin.readline())
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))

    lvl = 1

    up = move(board, UP, lvl)
    down = move(board, DOWN, lvl)
    left = move(board, LEFT, lvl)
    right = move(board, RIGHT, lvl)

    print(max(up, down, left, right))
