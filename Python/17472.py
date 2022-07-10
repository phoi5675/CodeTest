import sys
from collections import deque
import heapq


VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
INF = 1e9

if __name__ == '__main__':
    def make_label() -> int:
        Q = deque()
        index = 1

        for i in range(N):
            for j in range(M):
                if input_world[i][j]:
                    Q.append((i, j))
                    input_world[i][j] = 0
                    world[i][j] = index

                    while Q:
                        cur_i, cur_j = Q.popleft()

                        for dy, dx in VEC:
                            if 0 <= cur_i + dy < N and 0 <= cur_j + dx < M and \
                                    input_world[cur_i + dy][cur_j + dx]:
                                Q.append((cur_i + dy, cur_j + dx))
                                input_world[cur_i + dy][cur_j + dx] = 0
                                world[cur_i + dy][cur_j + dx] = index
                    index += 1

        return index - 1

    def make_graph() -> None:
        """
        Make graph for islands
        :return: None
        """
        for i in range(N):
            for j in range(M):
                if not world[i][j]:
                    continue
                for dy, dx in VEC:
                    ny, nx = i + dy, j + dx
                    bridge_len = 0
                    while 0 <= ny < N and 0 <= nx < M and world[ny][nx] == 0:
                        ny, nx = ny + dy, nx + dx
                        bridge_len += 1

                    if not 0 <= ny < N or not 0 <= nx < M:
                        continue
                    edge_1, edge_2 = world[i][j] - 1, world[ny][nx] - 1
                    if 2 <= bridge_len < graph[edge_1][edge_2] and \
                            world[ny][nx] and world[ny][nx] != world[i][j]:
                        graph[edge_1][edge_2] = graph[edge_2][edge_1] = bridge_len

    def prim() -> tuple:
        Q = []
        visited = [False] * islands
        visited[0] = True
        bridge_len = 0
        for i in range(islands):
            if graph[0][i] != INF:
                heapq.heappush(Q, (graph[0][i], i))

        while len(Q):
            cost, edge = heapq.heappop(Q)
            if visited[edge]:
                continue

            visited[edge] = True
            bridge_len += cost
            for i in range(islands):
                if graph[edge][i] != INF:
                    heapq.heappush(Q, (graph[edge][i], i))

        return bridge_len, False not in visited

    N, M = list(map(int, sys.stdin.readline().split()))
    res = INF
    input_world = []
    world = [[0] * M for _ in range(N)]
    for _ in range(N):
        input_world.append(list(map(int, sys.stdin.readline().split())))

    bridges = make_label() - 1
    islands = bridges + 1
    graph = [[INF] * islands for _ in range(islands)]
    make_graph()

    bridge_len, connected = prim()

    if not connected:
        print(-1)
    else:
        print(bridge_len)
