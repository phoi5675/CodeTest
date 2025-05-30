from typing import *


def solution(n: int, s: int) -> List[int]:
    # n보다 s가 작은 경우, 모든 집합의 원소가 1이더라도 s를 만들 수 없음
    if n > s:
        return [-1]
    
    q, l = s // n, s % n  # 몫, 나머지
    answer = [q] * n
    
    # 중복집합에서 최고의 집합은 나머지 l이 모든 수에 대해 최대한 공평하게 분배된 경우.
    # 즉, 집합의 원소 l개에 모두 공평하게 1씩 나머지 값을 나눠주는 경우가 가장 이상적임.
    for i in range(n - l, n):
        answer[i] += 1
    return answer