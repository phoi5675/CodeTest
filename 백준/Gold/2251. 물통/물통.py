from typing import *
from collections import deque

CAPACITY = 200 + 1

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    visited: List[List[List[bool]]] = [[[False] * CAPACITY for _ in range(CAPACITY)] for _ in range(CAPACITY)]
    ans: List[bool] = [False] * CAPACITY
    Q = deque()
    Q.append((0, 0, c))
    visited[0][0][c] = True

    while Q:
        a_filled, b_filled, c_filled = Q.popleft()
        if a_filled == 0:
            ans[c_filled] = True

        for i, (from_bucket, from_filled) in enumerate(zip((a, b, c), (a_filled, b_filled, c_filled))):
            for j, (to_bucket, to_filled) in enumerate(zip((a, b, c), (a_filled, b_filled, c_filled))):
                if i == j:
                    continue
                if from_filled > 0 and to_bucket > to_filled:
                    amount = to_bucket - to_filled if from_filled >= to_bucket - to_filled else from_filled
                    next_filled = [a_filled, b_filled, c_filled]
                    next_filled[i] = from_filled - amount
                    next_filled[j] = to_filled + amount
                    if not visited[next_filled[0]][next_filled[1]][next_filled[2]]:
                        visited[next_filled[0]][next_filled[1]][next_filled[2]] = True
                        Q.append(next_filled[:])

    print(*(idx for idx, filled in enumerate(ans) if filled), sep=' ')
