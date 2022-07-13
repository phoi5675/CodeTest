import sys

additional_lines = sys.maxsize
route_exists = False

if __name__ == "__main__":
    def simulate_ladder(_ladder: list) -> bool:
        global route_exists
        for point in range(n):
            x = point
            for y in range(h):
                x += _ladder[y][x]
            if x != point:
                return False

        route_exists = True
        return True


    def dfs_make_ladder(_ladder: list, cur_pos: list, added_lanes: int, depth_limit: int) -> None:
        global additional_lines
        # h -> y-axis, n -> x-axis
        y, x = cur_pos

        # visit
        if simulate_ladder(_ladder):
            print(added_lanes)
            exit(0)

        # terminal condition
        if added_lanes >= depth_limit or y >= h:
            return

        j = x
        while j < n - 1 and y < h:
            # traverse
            next_y, next_x = y, j + 2
            if next_x >= n - 1:
                next_y += 1
                next_x = 0
            # make ladder line
            # traverse when only if we can create new line
            if _ladder[y][j] == 0 and _ladder[y][j + 1] == 0 and added_lanes < depth_limit:
                copied_ladder = [line[:] for line in _ladder]
                copied_ladder[y][j], copied_ladder[y][j + 1] = TO_RIGHT, TO_LEFT
                added_lanes += 1
                dfs_make_ladder(copied_ladder, [next_y, next_x], added_lanes, depth_limit)
                # rollback added lines count after traverse
                added_lanes -= 1
                j += 1
            # can't make ladder line
            else:
                # skipping existing lane
                if _ladder[y][j] == 0 and _ladder[y][j + 1] != 0:
                    j += 3
                elif _ladder[y][j] != 0 and _ladder[y][j + 1] != 0:
                    j += 2
                else:
                    j += 1

            # move down
            if j >= n - 1:
                j = 0
                y += 1


    TO_LEFT, TO_RIGHT = -1, 1
    n, m, h = list(map(int, sys.stdin.readline().split()))
    ladder = [[0 for _ in range(n)] for _ in range(h)]

    # make initial ladder
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().split()))
        # make a, b from 1-index to 0-index
        a -= 1
        b -= 1
        ladder[a][b] = TO_RIGHT
        ladder[a][b + 1] = TO_LEFT

    for i in range(3 + 1):
        dfs_make_ladder(ladder, [0, 0], 0, i)

    print(-1)
