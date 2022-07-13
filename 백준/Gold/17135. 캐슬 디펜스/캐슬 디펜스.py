import copy
from collections import deque

VEC = ((0, -1), (-1, 0), (0, 1))    # left, up, right
Q = deque()
if __name__ == '__main__':
    def combination(idx: int, n: int, level: int, result: list) -> None:
        if level == 3:
            pos_of_archers.append(result[:])
            return

        for i in range(idx, n + 1):
            result.append(i)
            combination(i + 1, n, level + 1, result)
            result.pop()

        return

    def bfs(y: int, x: int, dist: int) -> tuple:
        global field
        ty = tx = -1
        td = 1e9
        Q.clear()
        Q.append((y, x, 1))
        visited[y][x] = True
        while Q:
            ny, nx, nd = Q.popleft()
            if field[ny][nx] and td > nd:
                ty, tx, td = ny, nx, nd

            for v in VEC:
                tmp_y, tmp_x = ny + v[0], nx + v[1]
                if 0 <= tmp_y < N and 0 <= tmp_x < M and nd + 1 <= dist and not visited[tmp_y][tmp_x]:
                    Q.append((tmp_y, tmp_x, nd + 1))
                    visited[tmp_y][tmp_x] = True

        return ty, tx


    N, M, D = list(map(int, input().split()))
    field = []
    pos_of_archers = []
    visited = [[False] * M for _ in range(N)]

    enemies_left = 0
    res = 0
    for _ in range(N):
        field.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                enemies_left += 1

    combination(0, M - 1, 0, [])
    copied_field = copy.deepcopy(field)
    copied_visited = copy.deepcopy(visited)

    for archers_list in pos_of_archers:
        e_left = enemies_left
        enemies_killed = 0
        field = copy.deepcopy(copied_field)
        for archer_y in range(N - 1, 0 - 1, -1):
            if e_left == 0:
                break
            spotted = set()
            # Find enemy near this archer
            for archer in archers_list:
                visited = copy.deepcopy(copied_visited)
                target_pos = bfs(archer_y, archer, D)
                # Add coord to set
                if target_pos[0] != -1:
                    spotted.add(target_pos)
            # Kill enemy
            for s in spotted:
                y, x = s
                field[y][x] = 0
                enemies_killed += 1

            e_left -= field[archer_y].count(1)

        # Compare number of killed enemies
        res = max(res, enemies_killed)

    print(res)
