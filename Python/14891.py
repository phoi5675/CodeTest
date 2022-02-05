import sys
import collections

if __name__ == "__main__":
    WH_ANGLES = 8
    STOP, CW, CCW = 0, 1, -1
    TOP, LEFT, RIGHT = 0, 2, 1
    chains = [[0] * 8]  # make index starting from 0 -> 1
    rotate_coms = []
    N, S = 0, 1
    # initial top, right, left index
    pos = [[0, 0, 0]]

    for _ in range(4):
        pos.append([0, 2, 6])
        inp = list(sys.stdin.readline())
        inp.pop()
        chains.append(list(map(int, inp)))

    k = int(sys.stdin.readline())

    for _ in range(k):
        rotate_coms.append(list(map(int, sys.stdin.readline().split())))

    for chain_num, rotate_order in rotate_coms:
        rotate_ary = [0] + [STOP] * 4

        rotate_ary[chain_num] = rotate_order
        # check left side of selected chain
        for left in range(chain_num, 1 - 1, -1):
            # rotate condition of left side of chain
            if chains[left][pos[left][LEFT]] != chains[left - 1][pos[left - 1][RIGHT]] and rotate_ary[left] != STOP:
                rotate_ary[left - 1] = CW if rotate_ary[left] == CCW else CCW

        # check right side of selected chain
        for right in range(chain_num, 4, 1):
            # rotate condition of left side of chain
            if chains[right][pos[right][RIGHT]] != chains[right + 1][pos[right + 1][LEFT]] and rotate_ary[right] != STOP:
                rotate_ary[right + 1] = CW if rotate_ary[right] == CCW else CCW

        # rotate chains
        for i in range(1, 4 + 1):
            if rotate_ary[i] == CW:
                for j in range(3):
                    pos[i][j] = (pos[i][j] + 8 - 1) % 8
            elif rotate_ary[i] == CCW:
                for j in range(3):
                    pos[i][j] = (pos[i][j] + 1) % 8

    total_score = 0
    for i in range(1, 4 + 1):
        score = 2 ** (i - 1) if chains[i][pos[i][TOP]] == S else 0
        total_score += score

    print(total_score)
