from copy import deepcopy
from typing import *

VEC = ((-1, 0), (0, -1), (1, 0), (0, 1))
WIDTH = 12
HEIGHT = 6

if __name__ == '__main__':
    def dfs(color: str, pos: Tuple[int, int]) -> None:
        for dy, dx in VEC:
            ny, nx = pos[0] + dy, pos[1] + dx
            if 0 <= ny < HEIGHT and 0 <= nx < WIDTH and puyo[ny][nx] == color and not visited[ny][nx]:
                visited[ny][nx] = True
                same_puyos.append((ny, nx))
                dfs(color, (ny, nx))

    puyo: List[List[str]] = [[] for _ in range(HEIGHT)]
    visited: List[List[bool]] = [[False] * WIDTH for _ in range(HEIGHT)]
    _visited = deepcopy(visited)
    same_puyos: List[Tuple[int, int]] = []
    booms = 0
    is_game_end = False

    for _ in range(WIDTH):
        hor = list(input())
        for idx, ch in enumerate(hor):
            puyo[idx].append(ch)

    while not is_game_end:
        is_booms: bool = False
        visited = deepcopy(_visited)
        # Search booms
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if not puyo[i][j].isalpha() or visited[i][j]:
                    continue
                visited[i][j] = True
                same_puyos.append((i, j))
                dfs(puyo[i][j], (i, j))

                if len(same_puyos) >= 4:
                    is_booms = True
                    for y, x in same_puyos:
                        puyo[y][x] = '-'
                same_puyos.clear()
        # Clean up boomed puyos
        for idx, line in enumerate(puyo):
            boomed = line.count('-')
            if boomed:
                puyo[idx] = ['.'] * boomed + [e for e in puyo[idx] if e != '-']
        if is_booms:
            is_game_end = False
            booms += 1
        else:
            is_game_end = True

    print(booms)
