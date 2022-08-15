from typing import *

if __name__ == '__main__':
    def dfs(idx: int, level: int) -> None:
        if level == 2:
            if height_sum - sum(hobbit for i, hobbit in enumerate(hobbits) if visited[i]) == 100:
                print(*sorted(hobbit for i, hobbit in enumerate(hobbits) if not visited[i]), sep='\n')
                exit(0)
            return

        for i in range(idx, 9):
            if not visited[i]:
                visited[i] = True
                dfs(i + 1, level + 1)
                visited[i] = False

    hobbits: List[int] = []
    visited: List[bool] = [False] * 9
    height_sum = 0

    for _ in range(9):
        hobbits.append(int(input()))

    height_sum = sum(hobbits)

    dfs(0, 0)
