import sys
import collections

if __name__ == "__main__":
    def dfs(elem: list, start: int, _k: int) -> None:
        if _k == 0:
            combination.append(tuple(elem[:]))  # copy elem
            return

        for i in range(start, n):
            elem.append(i)
            dfs(elem, i + 1, _k - 1)
            elem.pop()

    def calc_diff(team: list) -> int:
        all_members = [False] * n
        for start_mem in team:
            all_members[start_mem] = True
        diff = 0

        # calc stat difference
        for i in range(n):
            # members == true -> start team
            for j in range(i + 1, n):
                if all_members[i] and all_members[j]:
                    diff += (stat[i][j] + stat[j][i])
                if not all_members[i] and not all_members[j]:
                    diff -= (stat[i][j] + stat[j][i])

        return abs(diff)

    stat, combination = [], []
    min_stat_diff = sys.maxsize

    n = int(sys.stdin.readline())
    for _ in range(n):
        stat.append(list(map(int, sys.stdin.readline().split())))

    dfs([], 0, n // 2)  # make combination of start / link team
    stat_dict = {}

    for start_team in combination:
        # if stat of start team is in stat_dict, stat difference was already calc'd.
        if start_team in stat_dict:
            continue

        min_stat_diff = min(min_stat_diff, calc_diff(start_team))

    print(min_stat_diff)
