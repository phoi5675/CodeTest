import sys

if __name__ == "__main__":
    def move(ball_ch, ball_pos, hor: int, vert: int, other_ball_pos) -> list:
        coord = ball_pos.copy()
        while board[coord[1] + vert][coord[0] + hor] != "#" and [coord[0] + hor, coord[1] + vert] != other_ball_pos:
            coord[0] += hor
            coord[1] += vert

        return coord

    def is_reached_goal(coord, hor, vert) -> bool:
        if board[coord[1]][coord[0]] == "O":
            return True
        else:
            return False

    def dfs(depth: int, hor: int, vert: int, _red, _blue) -> int:
        # terminal condition
        if depth > 10:
            return -1
        x, y = _red
        # can't move
        if board[y + vert][x + hor] == "#" or board[y + vert][x + hor] == _blue:
            return 0

        # move red, blue
        _red = move("R", _red, hor, vert, _blue)
        if is_reached_goal(_red, hor, vert):
            return depth
        _blue = move("B", _blue, hor, vert, _red)
        if is_reached_goal(_blue, hor, vert):
            return -1

        # move blue, red
        _blue = move("B", _blue, hor, vert, _red)
        if is_reached_goal(_blue, hor, vert):
            return -1
        _red = move("R", _red, hor, vert, _blue)
        if is_reached_goal(_red, hor, vert):
            return depth

        up = down = left = right = 0
        if vert != DOWN:
            up = dfs(depth + 1, 0, UP, _red, _blue)
        if vert != UP:
            down = dfs(depth + 1, 0, DOWN, _red, _blue)
        if hor != RIGHT:
            left = dfs(depth + 1, LEFT, 0, _red, _blue)
        if hor != LEFT:
            right = dfs(depth + 1, RIGHT, 0, _red, _blue)

        has_route = max(up, down, left, right) > 0

        if has_route:
            res = 11
            for i in (up, down, left, right):
                if i > 0:
                    res = min(res, i)
            return res
        else:
            return -1

    n, m = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(n):
        board.append(list(sys.stdin.readline()))

    blue = red = goal = [0, 0]

    LEFT = UP = -1
    RIGHT = DOWN = 1

    # (x, y)
    # find pos of balls and goal
    for i, row in enumerate(board):
        for j, ch in enumerate(row):
            if ch == "#" or ch == ".":
                continue
            elif ch == "R":
                red = [j, i]
                board[i][j] = "."
            elif ch == "B":
                blue = [j, i]
                board[i][j] = "."
            elif ch == "O":
                goal = [j, i]

    up = dfs(1, 0, UP, red, blue)
    down = dfs(1, 0, DOWN, red, blue)
    left = dfs(1, LEFT, 0, red, blue)
    right = dfs(1, RIGHT, 0, red, blue)

    has_route = max(up, down, left, right) > 0

    if has_route:
        res = 11
        for i in (up, down, left, right):
            if i > 0:
                res = min(res, i)
        print(res)
    else:
        print(-1)
