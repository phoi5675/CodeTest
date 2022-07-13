import sys

if __name__ == "__main__":
    E, W, N, S = 1, 2, 3, 4
    TOP, NSIDE, ESIDE, WSIDE, FRONT, BOTTOM = [n for n in range(6)]

    dice = [0] * 6
    x_axis = [TOP, ESIDE, BOTTOM, WSIDE]
    y_axis = [TOP, NSIDE, BOTTOM, FRONT]

    game_map = []
    height, length, y, x, k = list(map(int, sys.stdin.readline().split()))
    for _ in range(height):
        game_map.append(list(map(int, sys.stdin.readline().split())))
    orders = list(map(int, sys.stdin.readline().split()))

    for order in orders:
        # north
        if order == N and (0 <= x < length and 0 <= y - 1 < height):
            # move dice
            dice[TOP], dice[NSIDE], dice[BOTTOM], dice[FRONT] = \
                dice[FRONT], dice[TOP], dice[NSIDE], dice[BOTTOM]
            y -= 1
        # south
        elif order == S and (0 <= x < length and 0 <= y + 1 < height):
            dice[TOP], dice[NSIDE], dice[BOTTOM], dice[FRONT] = \
                dice[NSIDE], dice[BOTTOM], dice[FRONT], dice[TOP]
            y += 1
        # west
        elif order == W and (0 <= x - 1 < length and 0 <= y < height):
            dice[WSIDE], dice[TOP], dice[ESIDE], dice[BOTTOM] = \
                dice[TOP], dice[ESIDE], dice[BOTTOM], dice[WSIDE]
            x -= 1
        # east
        elif order == E and (0 <= x + 1 < length and 0 <= y < height):
            dice[TOP], dice[ESIDE], dice[BOTTOM], dice[WSIDE] = \
                dice[WSIDE], dice[TOP], dice[ESIDE], dice[BOTTOM]
            x += 1
        else:
            continue

        if game_map[y][x] == 0:
            game_map[y][x] = dice[BOTTOM]
        else:
            dice[BOTTOM] = game_map[y][x]
            game_map[y][x] = 0

        print(dice[TOP])
