from typing import *
from collections import deque

MAX_LEN = 200_000 + 1
INF = int(1e9)

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    Q: Deque[Tuple[int, int]] = deque()
    dp: List[int] = [INF] * MAX_LEN
    Q.append((n, 0))
    dp[n] = 0

    while Q:
        pos, moves = Q.popleft()

        if pos == k:
            print(dp[k])
            exit(0)

        if 0 <= pos - 1 and moves + 1 < dp[pos - 1]:
            dp[pos - 1] = moves + 1
            Q.append((pos - 1, moves + 1))
        if pos + 1 < MAX_LEN and moves + 1 < dp[pos + 1]:
            dp[pos + 1] = moves + 1
            Q.append((pos + 1, moves + 1))
        if 2 * pos < MAX_LEN and moves + 1 < dp[2 * pos]:
            dp[2 * pos] = moves + 1
            Q.append((2 * pos, moves + 1))

