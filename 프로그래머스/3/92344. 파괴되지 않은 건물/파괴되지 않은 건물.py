from typing import *

HIT, HEAL = 1, 2

# https://tech.kakao.com/posts/488 를 참고하여 푼 문제
def solution(board: List[List[int]], skill: List[List[int]]):
    answer = 0
    r, c = len(board), len(board[0])
    skill_map: List[List[int]] = [[0] * (c + 1) for _ in range(r + 1)]
    
    for sk_type, r1, c1, r2, c2, deg in skill:
        _deg = deg if sk_type == HEAL else -deg
        # 부분합을 이용하여 문제 해결
        skill_map[r1][c1] += _deg
        skill_map[r1][c2 + 1] -= _deg
        skill_map[r2 + 1][c1] -= _deg
        skill_map[r2 + 1][c2 + 1] += _deg
    
    # 맵에 저장한 부분합을 가로 / 세로 각각 맵 전체로 적용
    for i in range(r + 1):
        for j in range(1, c + 1):
            skill_map[i][j] += skill_map[i][j - 1]
    for i in range(1, r + 1):
        for j in range(c + 1):
            skill_map[i][j] += skill_map[i - 1][j]
    
    # 살아남은 건물 확인
    for i in range(r):
        for j in range(c):
            building = board[i][j] + skill_map[i][j]
            if building > 0:
                answer += 1
    return answer