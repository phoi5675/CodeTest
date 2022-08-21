from typing import *
from collections import deque
from copy import deepcopy

INF = int(1e9)
P = -1

VEC = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)

if __name__ == '__main__':
    n = int(input())
    visited: List[List[int]] = [[INF] * n for _ in range(n)]
    _visited = deepcopy(visited)
    height_set: Set[int] = set()
    height_list: List[int] = []
    town_map: List[List[str]] = []
    height_map: List[List[int]] = []
    start: List[int] = []
    houses = 0
    res = INF

    left = right = 0
    max_house_height = 0

    for i in range(n):
        line = list(input())
        for j in range(n):
            if line[j] == 'P':
                start = [i, j]
            elif line[j] == 'K':
                houses += 1
        town_map.append(line)

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            height_set.add(line[j])
            if town_map[i][j] == 'K':
                max_house_height = max(max_house_height, line[j])
        height_map.append(line)

    height_list = sorted(list(height_set))

    right = max(height_list.index(max_house_height), height_list.index(height_map[start[0]][start[1]]))

    while left <= right < len(height_list) and \
            height_list[left] <= height_map[start[0]][start[1]] <= height_list[right]:
        reached_house = 0
        Q = deque()
        Q.append(start)
        diff = height_list[right] - height_list[left]
        visited[start[0]][start[1]] = diff

        while Q:
            y, x = Q.popleft()
            if town_map[y][x] == 'K':
                reached_house += 1

            for dy, dx in VEC:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] != diff and \
                        height_list[left] <= height_map[ny][nx] <= height_list[right]:
                    visited[ny][nx] = diff
                    Q.append((ny, nx))

        if reached_house < houses:
            right += 1
        elif reached_house == houses:
            res = min(res, diff)
            left += 1

    print(res)
