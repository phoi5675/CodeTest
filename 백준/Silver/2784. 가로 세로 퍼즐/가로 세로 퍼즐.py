from typing import *
from itertools import permutations

WORDS_LEN = 6

if __name__ == '__main__':
    words: List[str] = []
    for _ in range(WORDS_LEN):
        words.append(input())

    for (a, b, c) in permutations(range(0, WORDS_LEN), 3):
        visited: List[bool] = [False] * WORDS_LEN
        visited[a] = visited[b] = visited[c] = True
        count = 3
        for i in range(3):
            new_word = words[a][i] + words[b][i] + words[c][i]

            for idx, word in enumerate(words):
                if not visited[idx] and (word == new_word or reversed(word) == new_word):
                    visited[idx] = True
                    count += 1
                    break

        if count == WORDS_LEN:
            print(words[a], words[b], words[c], sep='\n')
            exit(0)

    print(0)
