import sys
from typing import *

def erase_center(n: int) ->  None:
    global N, stars 
    for i in range(N):
        for j in range(N):
            if (n // 3 <= int(i % n) < (2 * n) // 3) and \
                (n // 3 <= int(j % n) < (2 * n) // 3):
                stars[i][j] = ' '
    
    if (n > 3):
        erase_center(n / 3)

if __name__ == '__main__':
    N: int = int(input())
    stars: List[List[str]] = [['*' for _ in range(N)] for _ in range(N)]

    erase_center(N)
    for i in range(N):
        print("".join(stars[i]))
