if __name__ == '__main__':
    def is_readable(word: int) -> bool:
        global chars

        if word & chars == word:
            return True
        return False

    def dfs(depth: int, idx: int) -> None:
        global res, chars
        limit = K
        if depth == limit:
            readable = 0
            for word_bit in words_bits:
                if is_readable(word_bit):
                    readable += 1
            res = max(res, readable)
            return

        for i in range(idx, 26):
            if (chars >> i) & 1:
                continue

            chars = chars | 1 << i
            dfs(depth + 1, i + 1)
            chars = chars & ~(1 << i)

    res = 0

    N, K = list(map(int, input().split()))
    words_bits = []
    chars = 0
    for _ in range(N):
        w = input()
        bits = 0
        for ch in w:
            bits = bits | 1 << ord(ch) - ord('a')
        words_bits.append(bits)

    # Preprocess 'anta' and 'tica.'
    for ch in 'anta':
        chars = chars | 1 << ord(ch) - ord('a')

    for ch in 'tica':
        chars = chars | 1 << ord(ch) - ord('a')

    if K < 5:
        print(0)
    else:
        # 'acint' in 'anta' and 'tica' -> starts with 5 chars
        dfs(5, 0)

        print(res)
