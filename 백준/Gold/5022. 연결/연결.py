from typing import *
from collections import deque
from copy import deepcopy

INF = int(1e9)

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))


class Circuit:
    def __init__(self):
        self.circuit_len: int = 0
        self.is_valid: bool = False


if __name__ == '__main__':
    def bfs(start: List[int], dst: List[int], _visited: List[List[bool]]) -> int:
        queue: Deque[Tuple[int, int, int, list]] = deque()
        queue.append((start[0], start[1], 0, []))
        circuit[start[0]][start[1]] = True

        while queue:
            y, x, lines, traces = queue.popleft()

            if y == dst[0] and x == dst[1]:
                for t_y, t_x in traces:
                    circuit[t_y][t_x] = True
                return lines

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not _visited[ny][nx] and not circuit[ny][nx]:
                    _visited[ny][nx] = True
                    new_trace = traces[:]
                    new_trace.append((ny, nx))
                    queue.append((ny, nx, lines + 1, new_trace))

        return 0

    n, m = map(int, input().split())
    n += 1
    m += 1
    visited: List[List[bool]] = [[False] * m for _ in range(n)]
    circuit: List[List[bool]] = [[False] * m for _ in range(n)]
    _circuit = deepcopy(circuit)
    circuit_info = [Circuit(), Circuit()]
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    b1 = list(map(int, input().split()))
    b2 = list(map(int, input().split()))

    circuit_iter = [[a1, a2, b1, b2], [b1, b2, a1, a2]]

    for (p1, p2, q1, q2), c_info in zip(circuit_iter, circuit_info):
        circuit = deepcopy(_circuit)

        visited[q1[0]][q1[1]] = visited[q2[0]][q2[1]] = True
        bfs_1 = bfs(p1, p2, deepcopy(visited))
        visited[q1[0]][q1[1]] = visited[q2[0]][q2[1]] = False
        bfs_2 = bfs(q1, q2, deepcopy(visited))

        if bfs_1 and bfs_2:
            c_info.is_valid = True
            c_info.circuit_len = bfs_1 + bfs_2

    if circuit_info[0].is_valid and circuit_info[1].is_valid:
        print(min(circuit_info[0].circuit_len, circuit_info[1].circuit_len))
    elif circuit_info[0].is_valid or circuit_info[1].is_valid:
        print(circuit_info[0].circuit_len if circuit_info[0].is_valid else circuit_info[1].circuit_len)
    else:
        print("IMPOSSIBLE")
