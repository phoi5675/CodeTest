from typing import *
from collections import deque, defaultdict

VEC = ((-1, 0), (1, 0), (0, -1), (0, 1))

if __name__ == '__main__':
    def bfs(y: int, x: int) -> None:
        Q = deque()
        Q.append((y, x))

        while Q:
            y, x = Q.popleft()

            for dy, dx in VEC:
                ny, nx = dy + y, dx + x
                if 0 <= ny < R and 0 <= nx < C and cave[ny][nx] == 'x':
                    cave[ny][nx] = str(cluster_idx)
                    Q.append((ny, nx))
                    clusters[str(cluster_idx)].append((ny, nx))


    R, C = list(map(int, input().split()))
    cave: List[List[str]] = []
    spear_height: List[int] = []
    is_from_left: bool = True
    for _ in range(R):
        cave.append(list(input()))
    N = int(input())
    spear_height.extend(list(map(int, input().split())))

    for height in spear_height:
        start, end, step = (0, C, 1) if is_from_left else (C - 1, 0 - 1, -1)

        # Throw spear
        for i in range(start, end, step):
            if cave[R - height][i] == 'x':
                cave[R - height][i] = '.'
                break

        # Make clusters
        cluster_idx = 0
        clusters: DefaultDict[str, List[Tuple[int, int]]] = defaultdict(list)
        for i in range(R):
            for j in range(C):
                if cave[i][j] != 'x':
                    continue

                cave[i][j] = str(cluster_idx)
                clusters[str(cluster_idx)].append((i, j))
                bfs(i, j)
                cluster_idx += 1

        # Check non-floating clusters
        in_bottoms: Set[str] = set()
        for i in range(C):
            if cave[R - 1][i] != '.':
                in_bottoms.add(cave[R - 1][i])

        for cluster in clusters.keys():
            if cluster in in_bottoms:
                continue

            # Find moves for floating clusters
            moves = R - 1
            for y, x in clusters[cluster]:
                for ty in range(R - 1, y, -1):
                    if cave[ty][x] in in_bottoms:
                        moves = min(moves, ty - y - 1)
                    elif ty == R - 1:
                        moves = min(moves, R - y - 1)

            # Move clusters
            for y, x in clusters[cluster]:
                cave[y + moves][x] = 'x'

        # Re-draw cave with 'x'
        for i in range(R):
            for j in range(C):
                if cave[i][j] == '.':
                    continue
                elif cave[i][j] != 'x' and cave[i][j] not in in_bottoms:
                    cave[i][j] = '.'
                else:
                    cave[i][j] = 'x'

        # Change spear starting point
        is_from_left = not is_from_left

    for c in cave:
        print(''.join(c))
