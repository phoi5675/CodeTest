from heapq import *
from typing import *

def solution(n: int, works: List[int]):
    heap = []
    answer = 0
    
    for work in works:
        # heap은 작은 숫자 순서로 삽입되므로 큰 수를 우선 pop 하기 위해 key를 역순으로 삽입
        heappush(heap, (-work, work))
    
    for i in range(n):
        _, work = heappop(heap)
        
        if work > 0:
            work -= 1
        heappush(heap, (-work, work))
    
    for _, work in heap:
        answer += work ** 2
        
    return answer