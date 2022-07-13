import sys


if __name__ == '__main__':
    stations = []
    res = 0
    for _ in range(10):
        stations.append(list(map(int, sys.stdin.readline().split())))

    people_in_train = 0
    for outs, ins in stations:
        people_in_train -= outs
        people_in_train += ins
        res = people_in_train if res < people_in_train else res

    print(res)
