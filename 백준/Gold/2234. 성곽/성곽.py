from typing import *
from collections import deque

W, N, E, S = 0b1, 0b10, 0b100, 0b1000
VEC = ((0, -1), (-1, 0), (0, 1), (1, 0))
WALLS = (W, N, E, S)

if __name__ == '__main__':
    def bfs(i: int, j: int, room_id: int) -> int:
        rooms: int = 0
        Q = deque()
        Q.append((i, j))
        visited[i][j] = True

        while Q:
            y, x = Q.popleft()

            rooms += 1
            clustered_castle[y][x] = room_id

            for idx, (dy, dx) in enumerate(VEC):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and \
                        WALLS[idx] & castle[y][x] == 0:
                    visited[ny][nx] = True
                    Q.append((ny, nx))

        return rooms

    m, n = map(int, input().split())
    castle: List[List[int]] = []
    visited: List[List[bool]] = [[False] * m for _ in range(n)]
    clustered_castle: List[List[int]] = [[-1] * m for _ in range(n)]
    clustered_info: List[Tuple[int, int]] = []
    maximum_merged_room: int = 0

    room_id = 0

    for _ in range(n):
        castle.append(list(map(int, input().split())))

    # Cluster rooms
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                rooms = bfs(i, j, room_id)
                clustered_info.append((room_id, rooms))
                room_id += 1

    # Calculate maximum size of room if a wall is removed from the castle.
    for i in range(n):
        for j in range(m):
            for idx, (wall, (dy, dx)) in enumerate(zip(WALLS, VEC)):
                ny, nx = i + dy, j + dx
                if 0 <= ny < n and 0 <= nx < m and castle[i][j] & wall == wall and \
                        clustered_castle[i][j] != clustered_castle[ny][nx]:
                    room_1 = clustered_castle[i][j]
                    room_2 = clustered_castle[ny][nx]
                    maximum_merged_room = max(maximum_merged_room,
                                              clustered_info[room_1][1] + clustered_info[room_2][1])

    print(len(clustered_info))
    print(max(room[1] for room in clustered_info))
    print(maximum_merged_room)
