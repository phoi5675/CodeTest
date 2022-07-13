import sys
import itertools


if __name__ == '__main__':
    res = 0
    N = int(sys.stdin.readline())
    innings = []
    visited = [False] * 9
    # Init condition
    visited[1 - 1] = True
    order = [1 - 1]
    for _ in range(N):
        innings.append(list(map(int, sys.stdin.readline().split())))

    # Using permutation
    permutated = itertools.permutations(range(1, 9))
    for p in permutated:
        # Simulate game
        _order = list(p)
        _order.append(0)

        score = 0
        player_index = 0
        mask = 0xF0
        # Swap 1st and 4th player as 1st player is pre-allocated.
        _order[-1], _order[4 - 1] = _order[4 - 1], _order[-1]
        for inning in innings:
            out = 0
            base_status = 0
            while out < 3:
                player = inning[_order[player_index]]
                if player == 0:
                    out += 1
                else:
                    # Move players.
                    # Use 1-index
                    base_status = (base_status << player) + (1 << player)
                    if mask & base_status:
                        score += 1 & (base_status >> 4)
                        score += 1 & (base_status >> 5)
                        score += 1 & (base_status >> 6)
                        score += 1 & (base_status >> 7)

                        # Remove players hit home
                        base_status &= ~mask
                player_index = (player_index + 1) % 9
        res = max(res, score)

    print(res)
