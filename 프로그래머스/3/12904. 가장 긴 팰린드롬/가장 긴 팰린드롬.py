from typing import *


def solution(s: str) -> int:
    answer = 0

    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                answer = max(answer, len(substr))

    return answer