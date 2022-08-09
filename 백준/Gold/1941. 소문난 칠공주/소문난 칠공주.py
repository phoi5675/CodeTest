from typing import *
from copy import deepcopy
from collections import deque
from itertools import combinations

VEC = ((-1, 0), (1, 0), (0, 1), (0, -1))
CLASS_SIZE = 5
MEMBER_LIMIT = 7
res = 0

if __name__ == '__main__':
    def int_to_coord(_comb: List[int]) -> Tuple[List[Tuple], bool]:
        _members: List[Tuple] = []
        soms, lims = 0, 0
        for c in _comb:
            y = c // CLASS_SIZE
            x = c % CLASS_SIZE
            _members.append((y, x))
            soms += 1 if classroom[y][x] == 'S' else 0
            lims += 1 if classroom[y][x] == 'Y' else 0

        return _members, soms > lims

    def bfs(members: List[Tuple]) -> None:
        global res
        Q = deque()
        Q.append(members[0])
        connected = 0
        visited[members[0][0]][members[0][1]] = True

        while Q:
            y, x = Q.popleft()
            if connected == MEMBER_LIMIT - 1:
                res += 1
                return

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < CLASS_SIZE and 0 <= nx < CLASS_SIZE and not visited[ny][nx] and (ny, nx) in members:
                    visited[ny][nx] = True
                    Q.append((ny, nx))
                    connected += 1

    classroom: List[List[str]] = []
    visited: List[List[bool]] = [[False] * CLASS_SIZE for _ in range(CLASS_SIZE)]
    _visited = deepcopy(visited)
    for _ in range(CLASS_SIZE):
        classroom.append(list(input()))

    for comb in combinations(range(25), 7):
        members, is_soms_major = int_to_coord(comb)
        if is_soms_major:
            visited = deepcopy(_visited)
            bfs(members)

    print(res)
