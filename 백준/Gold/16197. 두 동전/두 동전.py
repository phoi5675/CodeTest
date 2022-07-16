from collections import deque
from copy import deepcopy

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
INF = 1e9
MAX_DEPTH = 10

if __name__ == '__main__':
    def coins_in_board(coins: list) -> int:
        num_of_coins_in = 0
        for coin in coins:
            y, x = coin
            if 0 <= y < N and 0 <= x < M:
                num_of_coins_in += 1

        return num_of_coins_in


    N, M = list(map(int, input().split()))
    board = []
    res = INF
    for _ in range(N):
        board.append(list(input()))

    coins = []
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                coins.append([i, j])

    Q = deque()
    Q.append((coins, (0, 0), 0))

    while Q:
        cur_coins, cur_v, depth = Q.popleft()
        if depth == MAX_DEPTH:
            continue
        coins_copied = deepcopy(cur_coins)
        for v in VEC:
            cur_coins = deepcopy(coins_copied)
            for i in range(len(cur_coins)):
                ny, nx = cur_coins[i][0] + v[0], cur_coins[i][1] + v[1]
                if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == '#':
                    continue
                cur_coins[i] = [ny, nx]

            if (0 <= cur_coins[0][0] < N and 0 <= cur_coins[0][1] < M and
                    0 <= cur_coins[1][0] < N and 0 <= cur_coins[1][1] < M and
                    visited[cur_coins[0][0]][cur_coins[0][1]][cur_coins[1][0]][cur_coins[1][1]]):
                continue
            num_of_coins_in = coins_in_board(cur_coins)
            if num_of_coins_in == 1 and depth + 1 <= MAX_DEPTH:
                res = min(res, depth + 1)
            elif num_of_coins_in == 2 and depth + 1 <= MAX_DEPTH:
                visited[cur_coins[0][0]][cur_coins[0][1]][cur_coins[1][0]][cur_coins[1][1]] = True
                Q.append((cur_coins, v, depth + 1))

    print(res if res != INF else -1)
