import sys
from collections import deque

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))

if __name__ == '__main__':
    N, M, speed = list(map(int, sys.stdin.readline().split()))
    ground = []
    visited = [[0] * M for _ in range(N)]
    res = 1e9
    for _ in range(N):
        ground.append(list(sys.stdin.readline()))

    start_y, start_x, dst_y, dst_x = list(map(int, sys.stdin.readline().split()))
    start_y -= 1
    start_x -= 1
    dst_y -= 1
    dst_x -= 1
    Q = deque()
    # (y, x, elapsed)
    Q.append((start_y, start_x, 0))
    visited[start_y][start_x] = True

    while Q:
        y, x, elapsed = Q.popleft()

        if y == dst_y and x == dst_x:
            res = min(elapsed, res)
            continue

        for dy, dx in VEC:
            for i in range(1, speed + 1):
                ny, nx = y + i * dy, x + i * dx
                if 0 <= ny < N and 0 <= nx < M:
                    if not visited[ny][nx] and ground[ny][nx] == '.':
                        visited[ny][nx] = elapsed + 1
                        Q.append((ny, nx, elapsed + 1))
                    elif visited[ny][nx] == elapsed + 1:
                        continue
                    elif ground[ny][nx] == '#':
                        break
                    else:
                        break
                else:
                    break

    if res == 1e9:
        print(-1)
    else:
        print(res)
