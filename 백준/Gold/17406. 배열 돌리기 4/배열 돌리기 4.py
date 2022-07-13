import sys
import copy


if __name__ == '__main__':
    def dfs(rots: list) -> None:
        global res
        limit = K
        if len(rots) == limit:
            # Simulate
            _ary = copy.deepcopy(ary)
            for rot in rots:
                r, c, s = rot
                width = 2 * s + 1
                i, j = r - s, c - s
                next_coord = (0, 1)
                tmp = _ary[i][j]
                while width > 1:
                    if i == r - s and j == c + s:
                        next_coord = (1, 0)
                    elif i == r + s and j == c + s:
                        next_coord = (0, -1)
                    elif i == r + s and j == c - s:
                        next_coord = (-1, 0)
                    _ary[i + next_coord[0]][j + next_coord[1]], tmp = \
                        tmp, _ary[i + next_coord[0]][j + next_coord[1]]
                    # Shrink rotation area
                    if i + next_coord[0] == r - s and j + next_coord[1] == c - s:
                        s -= 1
                        width -= 2
                        i, j = r - s, c - s
                        tmp = _ary[i][j]
                        next_coord = (0, 1)
                    else:
                        i += next_coord[0]
                        j += next_coord[1]

            # Calculate minimum
            res = min(res, min([sum(line) for line in _ary]))
            return

        for i in range(limit):
            if not visited[i]:
                visited[i] = True
                rots.append(rotations[i])
                dfs(rots)
                visited[i] = False
                rots.pop()

    N, M, K = list(map(int, sys.stdin.readline().split()))
    ary = []
    rotations = []
    visited = [False] * K
    res = 1e9
    for _ in range(N):
        ary.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(K):
        r, c, s = list(map(int, sys.stdin.readline().split()))
        # Convert 1-index to 0-index
        rotations.append([r - 1, c - 1, s])

    dfs([])

    print(res)
