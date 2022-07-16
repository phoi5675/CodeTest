if __name__ == '__main__':
    def is_minor(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


    def dfs(cur: int, depth: int) -> None:
        if depth == N:
            print(cur)
            return

        for i in range(1, 9 + 1, 2):
            candidate = 10 * cur + i
            if is_minor(candidate):
                dfs(candidate, depth + 1)


    N = int(input())

    minors = [2, 3, 5, 7]

    for minor in minors:
        dfs(minor, 1)
