import sys
import copy

blind_spot = sys.maxsize


if __name__ == "__main__":
    def erase_blind_spots(_office: list, cctv_pos: list, cctv_vec: list) -> int:
        UP, RIGHT, DOWN, LEFT = 1, 2, 3, 4
        erased = 0
        for vec in cctv_vec:
            y, x = 0, 0
            if vec == UP:
                y, x = -1, 0
            elif vec == RIGHT:
                y, x = 0, 1
            elif vec == DOWN:
                y, x = 1, 0
            elif vec == LEFT:
                y, x = 0, -1

            # delete blind spot in axis
            for axis in (y, x):
                cur_y, cur_x = cctv_pos[0] + y, cctv_pos[1] + x
                while axis and 0 <= cur_y < n and 0 <= cur_x < m:
                    if _office[cur_y][cur_x] == 6:
                        break
                    if _office[cur_y][cur_x] == 0:
                        _office[cur_y][cur_x] = "#"
                        erased += 1

                    cur_y += axis if y != 0 else 0
                    cur_x += axis if x != 0 else 0

        return erased


    def dfs(_office: list, zeroes: int, depth: int) -> None:
        global blind_spot
        if depth == num_of_cctv:
            blind_spot = min(zeroes, blind_spot)
            return

        y, x, cctv_type = cams[depth]
        for vec in vectors[cctv_type]:
            copied_office = copy.deepcopy(_office)
            erased = erase_blind_spots(copied_office, [y, x], vec)
            dfs(copied_office, zeroes - erased, depth + 1)

    office = []
    num_of_cctv = 0
    cams = []
    # vector = 1 : up, 2 : right, 3 : down, 4 : left
    vectors = [[],
               [[1], [2], [3], [4]],
               [[1, 3], [2, 4]],
               [[1, 2], [2, 3], [3, 4], [4, 1]],
               [[1, 2, 3], [2, 3, 4], [3, 4, 1], [4, 1, 2]],
               [[1, 2, 3, 4]]
               ]

    n, m = list(map(int, sys.stdin.readline().split()))
    for _ in range(n):
        office.append(list(map(int, sys.stdin.readline().split())))

    # find cctv positions and type
    for i in range(n):
        for j in range(m):
            cur_type = office[i][j]
            if 1 <= cur_type <= 5:
                cams.append([i, j, cur_type])

    num_of_cctv = len(cams)
    dfs(office, sum(line.count(0) for line in office), 0)

    print(blind_spot)
