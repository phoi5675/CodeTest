import sys
import heapq
import collections

if __name__ == "__main__":
    n, m, k = list(map(int, sys.stdin.readline().split()))

    s2d2_fertilizer = []
    fertilized_info = []
    trees = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(collections.deque())
        trees.append(row)

    # init s2d2 info and farm fertilized info
    for _ in range(n):
        s2d2_fertilizer.append(list(map(int, sys.stdin.readline().split())))
    fertilized_info = [[5] * n for _ in range(n)]

    for _ in range(m):
        y, x, age = list(map(int, sys.stdin.readline().split()))
        # make coords to 0-index
        trees[y - 1][x - 1].appendleft(age)

    for elapsed_year in range(k):
        breed_coord = collections.defaultdict(int)
        # spring
        # trees get fertilized starting from young trees to old ones
        for i in range(n):
            for j in range(n):
                for idx, tree in enumerate(trees[i][j]):
                    if tree <= fertilized_info[i][j]:
                        fertilized_info[i][j] -= tree
                        trees[i][j][idx] += 1
                        # if age of tree is multiple of 5, add it to breeding list at autumn
                        if trees[i][j][idx] % 5 == 0:
                            breed_coord[(i, j)] += 1
                    # if old ones could not get fertilized, it is removed from list and moved to dead queue
                    else:
                        for _ in range(idx, len(trees[i][j])):
                            # summer
                            fertilized_info[i][j] += trees[i][j].pop() >> 1
                        break

        for i in range(n):
            for j in range(n):
                # winter
                # s2d2 add fertilizers into farm
                fertilized_info[i][j] += s2d2_fertilizer[i][j]
                # autumn
                # reproduce trees
                if breed_coord[(i, j)] >= 1:
                    seed_range = [
                        [-1, -1], [-1, 0], [-1, 1],
                        [0, -1], [0, 1],
                        [1, -1], [1, 0], [1, 1]
                    ]
                    for (seed_y, seed_x) in seed_range:
                        dy, dx = i + seed_y, j + seed_x
                        if 0 <= dy < n and 0 <= dx < n:
                            for _ in range(breed_coord[(i, j)]):
                                trees[dy][dx].appendleft(1)

    # after k years, count remaining trees
    num_of_trees = 0
    for i in range(n):
        for j in range(n):
            num_of_trees += len(list(trees[i][j]))

    print(num_of_trees)
