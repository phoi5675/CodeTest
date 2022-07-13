import sys
import collections

if __name__ == "__main__":
    def get_back_side() -> list:
        N, W, S, E = 0, 1, 2, 3
        if vec == N:
            _back = DOWN
        elif vec == S:
            _back = UP
        elif vec == W:
            _back = RIGHT
        else:
            _back = LEFT
        return _back

    def is_clean_finished() -> bool:
        # check all direction has been cleaned or wall
        for vector in vectors:
            if house[y + vector[1]][x + vector[0]] == EMPTY:
                return False

        return True

    def vector_preprocess(_vec):
        N, E, S, W = 0, 1, 2, 3
        if _vec == N:
            return 0
        elif _vec == E:
            return 3
        elif _vec == S:
            return 2
        else:
            return 1

    house = []
    N, E, S, W = 0, 1, 2, 3
    rotate = [N, W, S, E]

    LEFT, RIGHT, UP, DOWN = [-1, 0], [1, 0], [0, -1], [0, 1]  # (x, y)
    vectors = [LEFT, DOWN, RIGHT, UP]
    EMPTY, CLEARED, WALL = 0, -1, 1
    cleared_tiles = 0

    n, m = map(int, sys.stdin.readline().split())
    y, x, vec = map(int, sys.stdin.readline().split())
    for _ in range(n):
        house.append(list(map(int, sys.stdin.readline().split())))

    vec = vector_preprocess(vec)

    while True:
        # clear current location
        if house[y][x] == EMPTY:
            house[y][x] = CLEARED
            cleared_tiles += 1

        # search location needs to be cleared from the left side
        left_side_y, left_side_x = vectors[vec][1], vectors[vec][0]
        back = get_back_side()
        # a. case
        if house[y + left_side_y][x + left_side_x] == EMPTY:
            # rotate
            vec = (vec + 1) % 4
            # move robot
            y += left_side_y
            x += left_side_x
            continue

        elif is_clean_finished():
            # c. case
            if house[y + back[1]][x + back[0]] != WALL:
                y += back[1]
                x += back[0]
                continue
            # d. case
            elif house[y + back[1]][x + back[0]] == WALL:
                break
        # b. case
        elif house[y + left_side_y][x + left_side_x] == CLEARED or house[y + left_side_y][x + left_side_x] == WALL:
            # rotate only
            vec = (vec + 1) % 4
            continue

    print(cleared_tiles)
