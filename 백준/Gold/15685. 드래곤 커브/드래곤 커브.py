import sys


if __name__ == "__main__":
    def convert_vec_to_coord(vec: int) -> tuple:
        """
        :param vec: 0 to 3 equivalent to right, up, left, down
        :return: (y,x) value to calculate new position of dragon's curve
        """
        # right
        if vec == 0:
            return 0, 1
        # up
        elif vec == 1:
            return -1, 0
        # left
        elif vec == 2:
            return 0, -1
        # down
        else:
            return 1, 0

    def rotate(vec: int) -> int:
        return (vec + 1) % 4

    def make_tail(_y: int, _x: int, _vec: int) -> tuple:
        dy, dx = convert_vec_to_coord(_vec)
        return _y + dy, _x + dx

    # make dragon and mark them on tile in one function to reduce exec time.
    def make_dragon_and_tile(_dragon) -> None:
        _x, _y, _d, _g = _dragon
        tail_y, tail_x = convert_vec_to_coord(_d)

        # make 0th gen and mark them on tiles
        dragon_body = [(_y, _x, _d), (_y + tail_y, _x + tail_x, rotate(_d))]
        for body in dragon_body:
            body_y, body_x, _ = body
            tiles[body_y][body_x] = True

        if _g == 0:
            return

        # make nth gen and mark them on tiles
        for gen in range(1, _g):
            new_body = []
            for body in reversed(dragon_body):
                # calculate position of head from existing tail
                if new_body:
                    tail_y, tail_x, vec = new_body[-1]
                else:
                    tail_y, tail_x, vec = dragon_body[-1]
                new_head_y, new_head_x = make_tail(tail_y, tail_x, vec)

                # rotate vector and add to new_body
                if new_body:
                    vec = body[2]
                rotated_vec = rotate(vec)
                new_body.append((new_head_y, new_head_x, rotated_vec))

                # mark new start to tiles
                tiles[new_head_y][new_head_x] = True

            # copy new body to existing body
            dragon_body += new_body[:]

        # add last tail to new_body
        tail_y, tail_x, vec = dragon_body[-1]
        new_head_y, new_head_x = make_tail(tail_y, tail_x, vec)
        # mark new start to tiles
        tiles[new_head_y][new_head_x] = True

    R, U, L, D = 0, 1, 2, 3
    # use 1-base indexing
    TILE_LEN = 100 + 1
    tiles = [[False for _ in range(TILE_LEN)] for _ in range(TILE_LEN)]
    dragons = []
    rect_by_dragons = 0
    n = int(sys.stdin.readline())
    # get info for dragons
    for _ in range(n):
        x, y, d, g = list(map(int, sys.stdin.readline().split()))
        dragons.append([x, y, d, g])

    for dragon in dragons:
        make_dragon_and_tile(dragon)

    # count tiles surrounded by dragon
    for i in range(TILE_LEN - 1):
        for j in range(TILE_LEN - 1):
            if tiles[i][j] and tiles[i][j + 1] and tiles[i + 1][j] and tiles[i + 1][j + 1]:
                rect_by_dragons += 1

    print(rect_by_dragons)
