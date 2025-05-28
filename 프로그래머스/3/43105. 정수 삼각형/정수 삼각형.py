from typing import *

def solution(triangle: List[List[int]]):
    # 삼각형 높이가 1인 경우
    if len(triangle) == 1:
        return triangle[0][0]
    
    dp: List[List[int]] = []
    for elems in triangle:
        dp.append([0] * len(elems))
        
    # 초기조건
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle) - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
        
    answer = max(dp[len(dp) - 1])
    return answer
