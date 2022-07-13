from collections import deque

INIT_SIZE = 2
VEC = ((-1, 0), (0, -1), (1, 0), (0, 1))  # up, left, down, right
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
MAX_INT = 9876543210

if __name__ == '__main__':
    def bfs(y: int, x: int) -> tuple:
        global fish_eaten, shark_size, edible
        fy = fx = fd = MAX_INT

        Q = deque()
        Q.append((y, x, 0))
        visited = [[False] * N for _ in range(N)]

        while len(Q):
            (_y, _x, t) = Q.popleft()
            if t > fd:
                continue
            # Check this space has fish
            if 0 < space[_y][_x] < shark_size and t <= fd:
                if _y < fy or (_y == fy and _x < fx):
                    fy, fx, fd = _y, _x, t

            # traverse
            for (dy, dx) in VEC:
                ny = dy + _y
                nx = dx + _x
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] \
                        and space[ny][nx] <= shark_size:
                    Q.append((ny, nx, t + 1))
                    visited[ny][nx] = True

        return fy, fx, fd


    elapsed = 0
    edible = 0
    fishes = [0] * 7

    shark_pos = [0, 0]
    shark_size = INIT_SIZE
    fish_eaten = 0

    # Get input.
    N = int(input())
    space = list()
    for _ in range(N):
        space.append(list(map(int, input().split())))

    # Find shark and fish
    for i in range(N):
        for j in range(N):
            if 0 < space[i][j] <= 6:
                fishes[space[i][j]] += 1
                if 0 < space[i][j] < INIT_SIZE:
                    edible += 1
            elif space[i][j] == 9:
                shark_pos = (i, j)
                space[i][j] = 0

    while edible:
        y, x, d = bfs(shark_pos[0], shark_pos[1])

        if d == MAX_INT:
            break

        # Move shark
        shark_pos = (y, x)
        elapsed += d

        # Eat fish.
        # If eat fish, reset queue.
        if 0 < space[y][x] < shark_size:
            space[y][x] = 0
            fish_eaten += 1
            edible -= 1

        # Check shark can grow up
        if shark_size == fish_eaten:
            shark_size += 1
            fish_eaten = 0
            if shark_size <= 7:
                edible += fishes[shark_size - 1]

    print(elapsed)
