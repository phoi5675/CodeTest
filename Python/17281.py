import sys


if __name__ == '__main__':
    def dfs(_visited: list, _order: list) -> None:
        global res
        if len(_order) == 9:
            # Simulate game
            score = 0
            player_index = 0
            mask = 0xF0
            # Swap 1st and 4th player as 1st player is pre-allocated.
            _order[1 - 1], _order[4 - 1] = _order[4 - 1], _order[1 - 1]
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
            # Rollback swap
            _order[1 - 1], _order[4 - 1] = _order[4 - 1], _order[1 - 1]
            return

        # Make combination
        for i in range(9):
            if not _visited[i]:
                _visited[i] = True
                _order.append(i)
                dfs(_visited, _order)
                _visited[i] = False
                _order.pop()

    res = 0
    N = int(sys.stdin.readline())
    innings = []
    visited = [False] * 9
    # Init condition
    visited[1 - 1] = True
    order = [1 - 1]
    for _ in range(N):
        innings.append(list(map(int, sys.stdin.readline().split())))

    dfs(visited, order)

    print(res)
