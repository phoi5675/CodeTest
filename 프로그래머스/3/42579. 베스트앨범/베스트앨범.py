from typing import *
from collections import defaultdict


def solution(genres: List[str], plays: List[int]):
    answer = []
    
    genres_dict: DefaultDict[str, Tuple[int, int]] = defaultdict(list)
    genres_sum: DefaultDict[str, int] = defaultdict(int)
    genres_list: List[Tuple[int, str]] = []
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # 장르를 key, (재생 횟수, 인덱스)를 value로 하는 딕셔너리 생성
        genres_dict[genre].append((play, idx))
        # 장르별 총 플레이 횟수 저장 딕셔너리
        genres_sum[genre] += play
    # 장르별 총 플레이 횟수를 저장한 딕셔너리를 리스트로 변환
    for genre, play_sum in genres_sum.items():
        genres_list.append((play_sum, genre))
    
    # 장르를 재생된 횟수 순서로 내림차순 정렬
    genres_list.sort(key=lambda x: x[0], reverse=True)
    
    for _, genre in genres_list:
        # 장르 정리한 딕셔너리에 대해, 재생 횟수는 오름차순, 인덱스는 내림차순 정렬
        genres_dict[genre].sort(key=lambda x: (-x[0], x[1]))
        for i, (play, idx) in enumerate(genres_dict[genre]):
            # 한 장르에 최대 수록 가능한 노래 개수는 2개이므로, 2개 초과 시 해당 장르 스킵
            if i >= 2:
                break
            answer.append(idx)
            
    return answer
