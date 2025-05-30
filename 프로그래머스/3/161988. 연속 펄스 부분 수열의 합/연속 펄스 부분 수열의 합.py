from typing import *


def solution(sequence: List[int]):
    n = len(sequence)
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(2)]  # (1, -1)인 경우에 대해 2차원 배열 형태로 dp 생성
    dp[0][0] = sequence[0]
    dp[1][0] = -sequence[0]
    
    for i in range(1, n):
        pos_pulse = 1 if i % 2 == 0 else -1
        neg_pulse = -pos_pulse  # dp[1]에서 쓰이는 (-) 펄스는 pos_pulse와 부호만 반대이므로 별도 연산 사용 X
        
        dp[0][i] = max(sequence[i] * pos_pulse, dp[0][i - 1] + sequence[i] * pos_pulse)
        dp[1][i] = max(sequence[i] * neg_pulse, dp[1][i - 1] + sequence[i] * neg_pulse)
    
    answer = max(max(dp[0]), max(dp[1]))
    return answer