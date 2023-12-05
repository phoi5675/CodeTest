from typing import *


def find(union: List[int], x) -> int:
    if (union[x] == x):
        return x
    else:
        union[x] = find(union, union[x])
        return union[x]

def make_union(union: List[int], x: int, y: int) -> None:
    x = find(union, x)
    y = find(union, y)

    if x < y:
        union[y] = x
    else:
        union[x] = y

def is_connected(union: List[int], x: int, y: int) -> bool:
    if find(union, x) == find(union, y):
        return True
    else:
        return False


def solution(n, costs):
    costs.sort(key=lambda cost: cost[2]) # 거리순으로 오름차순 정렬
    union: List[int] = [i for i in range(n)]
    edges = 0
    answer = 0

    for fr, to, cost in costs:
        if edges == n - 1:
            break

        if is_connected(union, fr, to):
            continue
        make_union(union, fr, to)
        answer += cost

    return answer
