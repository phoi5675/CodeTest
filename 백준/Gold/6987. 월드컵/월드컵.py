from typing import *

WIN, DRAW, LOSE = 0, 1, 2
is_right: bool = False

if __name__ == '__main__':
    def dfs(level: int) -> None:
        global is_right
        if is_right:
            return
        if level == 15:
            for t, g in zip(traverse, game_result):
                if t != g:
                    return
            is_right = True
            return

        t1, t2 = combination[level]

        match_res = ((WIN, LOSE), (DRAW, DRAW), (LOSE, WIN))
        for t1_res, t2_res in match_res:
            if traverse[3 * t1 + t1_res] < game_result[3 * t1 + t1_res] and \
                    traverse[3 * t2 + t2_res] < game_result[3 * t2 + t2_res]:
                traverse[3 * t1 + t1_res] += 1
                traverse[3 * t2 + t2_res] += 1
                dfs(level + 1)
                traverse[3 * t1 + t1_res] -= 1
                traverse[3 * t2 + t2_res] -= 1

    combination: List[Tuple[int, int]] = []
    for i in range(6):
        for j in range(i + 1, 6):
            combination.append((i, j))
    for _ in range(4):
        game_result: List[int] = list(map(int, input().split()))
        traverse = [0] * len(game_result)
        is_right = False

        dfs(0)
        if is_right:
            print(1, end=' ')
        else:
            print(0, end=' ')

