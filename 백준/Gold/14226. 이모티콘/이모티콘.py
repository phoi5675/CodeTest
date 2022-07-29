from typing import *
from collections import deque

MAX_SIZE = 1000 + 1
if __name__ == '__main__':
    S = int(input())
    Q: Deque[Tuple[int, int, int]] = deque()
    visited: List[List[bool]] = [[False] * MAX_SIZE for _ in range(MAX_SIZE)]
    visited[1][0] = True
    Q.append((1, 0, 0))
    res: int = 0
    while Q:
        emojis, clipboard, elapsed = Q.popleft()

        if emojis == S:
            res = elapsed
            break

        # Copy all emojis to clipboard
        if not visited[emojis][emojis]:
            visited[emojis][emojis] = True
            Q.append((emojis, emojis, elapsed + 1))

        # Paste emojis from clipboard
        if clipboard and emojis + clipboard < MAX_SIZE and \
                not visited[emojis + clipboard][clipboard]:
            visited[emojis + clipboard][clipboard] = True
            Q.append((emojis + clipboard, clipboard, elapsed + 1))

        # Delete one emoji from screen
        if emojis > 1 and not visited[emojis - 1][clipboard]:
            visited[emojis - 1][clipboard] = True
            Q.append((emojis - 1, clipboard, elapsed + 1))

    print(res)
