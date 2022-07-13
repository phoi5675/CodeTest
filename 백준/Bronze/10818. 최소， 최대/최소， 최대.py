if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    print('{0} {1}'.format(min(nums), max(nums)))
