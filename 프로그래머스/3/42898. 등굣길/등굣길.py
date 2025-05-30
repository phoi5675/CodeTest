from typing import *


WATER, EMPTY = 0, 1

def solution(m: int, n: int, puddles: List[List[int]]) -> int:
    answer = 0
    path_map: List[List[int]] = [[EMPTY] * (m + 1) for _ in range(n + 1)]
    dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    
    for x, y in puddles:  # puddles는 (x, y) 구조로 주어지므로 (y, x)대신 이러한 순서로 사용
        path_map[y][x] = WATER
    
    # 가로, 세로 일직선 방향에 대해서는 진행 가능한 경우의 수가 1개만 존재하므로 해당 경로 초기화
    # 다만 해당 길에 물웅덩이가 있는 경우, 그 아래로는 더 이상 진행할 수 없으므로 루프 빠져나옴
    for i in range(1, m + 1):
        if path_map[1][i] == WATER:
            break
        dp[1][i] = 1
    for i in range(1, n + 1):
        if path_map[i][1] == WATER:
            break
        dp[i][1] = 1
        
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            # 물 웅덩이가 있는 지점에 대해서는 dp 계산하지 않음
            if path_map[i][j] == WATER:
                continue
            # 아닌 경우에는 현재 지점 기준 위쪽, 왼쪽의 누적 경로 합을 저장
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    answer = dp[n][m] % 1_000_000_007
    return answer
