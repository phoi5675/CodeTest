if __name__ == '__main__':
    def dfs(i: int, accumulated: int, limit: int) -> None:
        global res
        if i >= limit:
            res = max(res, accumulated)
            return

        if i + 1 < limit:
            acc_1 = eval(str(accumulated) + equation[i] + equation[i + 1])
            dfs(i + 2, acc_1, limit)
        if i + 3 < limit:
            tmp = eval(equation[i + 1] + equation[i + 2] + equation[i + 3])
            acc_2 = eval(str(accumulated) + equation[i] + str(tmp))
            dfs(i + 4, acc_2, limit)

    N = int(input())
    equation = input()
    res = -1e9

    if N < 5:
        print(eval(equation))
    else:
        acc_1 = eval(equation[0] + equation[1] + equation[2])
        tmp = eval(equation[2] + equation[3] + equation[4])
        acc_2 = eval(equation[0] + equation[1] + str(tmp))
        dfs(3, acc_1, len(equation))
        dfs(5, acc_2, len(equation))
        print(res)
