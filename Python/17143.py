import copy

VEC = ((0, 0), (-1, 0), (1, 0), (0, 1), (0, -1))
UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4


class Fish:
    def __init__(self, s: int, d: int, z: int):
        self.speed = s
        self.direc = d
        self.size = z
        self.turn = 0


if __name__ == '__main__':
    def flip(vec: int) -> int:
        if vec == UP:
            return DOWN
        elif vec == DOWN:
            return UP
        elif vec == RIGHT:
            return LEFT
        else:
            return RIGHT

    def move_fish(r: int, c: int, fish: Fish) -> tuple:
        distance_left = fish.speed
        nr, nc = r, c
        for _ in range(distance_left):
            tr, tc = nr + VEC[fish.direc][0], nc + VEC[fish.direc][1]
            if not (1 <= tr <= R) or not (1 <= tc <= C):
                fish.direc = flip(fish.direc)
            nr, nc = nr + VEC[fish.direc][0], nc + VEC[fish.direc][1]

        return nr, nc

    R, C, M = list(map(int, input().split()))
    field = [[None for _ in range(C + 1)] for _ in range(R + 1)]
    max_turn = C
    sum_of_fish = 0
    empty_field = [[None for _ in range(C + 1)] for _ in range(R + 1)]
    for _ in range(M):
        r, c, s, d, z = list(map(int, input().split()))
        # Preprocess for speed >= 2 * (n - 1)
        if d == UP or d == DOWN:
            n = R
        else:
            n = C
        s = int(s % (2 * (n - 1)))
        field[r][c] = Fish(s, d, z)

    for fisherman_pos in range(1, max_turn + 1):
        # Fisherman catches fish
        for _r in range(1, R + 1):
            if field[_r][fisherman_pos] is not None:
                sum_of_fish += field[_r][fisherman_pos].size
                field[_r][fisherman_pos] = None
                break

        new_field = copy.deepcopy(empty_field)
        # Fish move
        for _r in range(1, R + 1):
            for _c in range(1, C + 1):
                if field[_r][_c] is not None:
                    nr, nc = move_fish(_r, _c, field[_r][_c])

                    if new_field[nr][nc] is None or \
                            (new_field[nr][nc] is not None and new_field[nr][nc].size < field[_r][_c].size):
                        new_field[nr][nc] = field[_r][_c]

        field = new_field

    print(sum_of_fish)