import sys
from collections import deque
import itertools


if __name__ == '__main__':
    def bfs(ary: list) -> tuple:
        connected = 1
        pop_sum = 0
        visited = [False] * (N + 1)
        first = ary[0]
        Q = deque()
        Q.append(first)
        visited[first] = True
        pop_sum += population[first]

        while Q:
            cur = Q.popleft()

            for edge in ary:
                if not visited[edge] and conns[edge][cur]:
                    visited[edge] = True
                    connected += 1
                    pop_sum += population[edge]
                    Q.append(edge)

        return connected, pop_sum

    N = int(sys.stdin.readline())
    population = [0] + list(map(int, sys.stdin.readline().split()))
    conns = [[0] * (N + 1) for _ in range(N + 1)]
    res = 1e9

    for i in range(1, N + 1):
        con_info = list(map(int, sys.stdin.readline().split()))
        for j in con_info[1:]:
            conns[i][j] = 1
            conns[j][i] = 1

    for i in range(1, N // 2 + 1):
        combinations = itertools.combinations(range(1, N + 1), i)

        for combination in combinations:
            red, red_sum = bfs(combination)
            blue, blue_sum = bfs([j for j in range(1, N + 1) if j not in combination])

            if red + blue == N:
                res = min(res, abs(red_sum - blue_sum))

    if res == 1e9:
        print(-1)
    else:
        print(res)
