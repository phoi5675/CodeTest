from typing import *
from copy import deepcopy
from collections import defaultdict, deque

def make_graph(tickets: List[List[str]]) -> Dict[str, List[str]]:
    graph: Dict[str, List[str]] = defaultdict(list)
    # 출발지, 도착지에 대해 그래프 생성
    for ticket in tickets:
        dept, arrv = ticket[0], ticket[1]
        graph[dept].append(arrv)
    
    # TODO: 주석 추가
    for key in graph.keys():
        graph[key] = sorted(graph[key])
    return graph
    
    
def dfs(limit: int, cur_city: str, visited: List[str], graph: Dict[str, List[str]]) -> List[str]:
    if len(visited) == limit:
        return visited
    
    for idx, city in enumerate(graph[cur_city]):
        if graph[cur_city][idx] == "-1":
            continue
        visited.append(city)
        next_city = city
        graph[cur_city][idx] = "-1"
        ans = dfs(limit, next_city, visited, graph)
        if ans:
            return ans
        graph[cur_city][idx] = next_city
        visited.pop()
    return None
    

    
def solution(tickets):
    graph = make_graph(tickets)
    answer = dfs(len(tickets) + 1, "ICN", ["ICN"], graph)
    return answer
