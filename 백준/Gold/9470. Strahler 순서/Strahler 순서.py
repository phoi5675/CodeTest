import sys
from collections import deque
from typing import *

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        K, M, P = list(map(int, sys.stdin.readline().split()))
        graph: List[List[int]] = [[] for _ in range(M + 1)]
        # [max. of current strahler, num of strahler, strahler of this node]
        state = [[1, 0, 1] for _ in range(M + 1)]
        indegree = [0] * (M + 1)

        for _ in range(P):
            start, end = list(map(int, sys.stdin.readline().split()))
            graph[start].append(end)
            indegree[end] += 1

        Q = deque()
        for i in range(1, M + 1):
            if indegree[i] == 0:
                Q.append(i)

        while Q:
            now = Q.popleft()

            for g in graph[now]:
                indegree[g] -= 1
                if state[now][2] == state[g][0]:
                    state[g][1] += 1
                    if state[g][1] == 2:
                        state[g][2] = state[now][2] + 1
                elif state[now][2] > state[g][0]:
                    state[g][1] = 1
                    state[g][0] = state[now][2]
                    state[g][2] = state[now][2]

                if indegree[g] == 0:
                    Q.append(g)

        print(K, state[M][2])
