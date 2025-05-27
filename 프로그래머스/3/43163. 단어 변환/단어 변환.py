from typing import * 
from collections import deque
from copy import deepcopy

def is_similar(a: str, b: str) -> bool:
    similar_cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            similar_cnt += 1
    
    # 현재 단어가 바꾸려는 단어와 다른 글자가 한 개만 있는지 확인
    return similar_cnt == len(a) - 1    

def solution(begin: str, target: str, words: List[str]):
    # 기본 종료 조건. target이 words에 없는 경우에는 단어 변환 불가능함
    if target not in words:
        return 0
    
    answer = 0
    q: Deque[int, str, List[bool]] = deque()
    q.append((0, begin, [False] * len(words))) # (변환 횟수, 방문 여부)
    
    while q and answer == 0:
        changed, cur_word, visited = q.popleft()
        for i in range(len(visited)):
            if not visited[i] and is_similar(cur_word, words[i]):
                if words[i] == target:
                    answer = changed + 1
                    
                visited_copy = deepcopy(visited)
                visited_copy[i] = True
                q.append((changed + 1, words[i], visited_copy))
                
    return answer
