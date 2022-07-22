NUMS = [
    0b11111_10001_11111,
    0b11111,
    0b10111_10101_11101,
    0b10101_10101_11111,
    0b11100_00100_11111,
    0b11101_10101_10111,
    0b11111_10101_10111,
    0b10000_10000_11111,
    0b11111_10101_11111,
    0b11101_10101_11111
]
THRESHOLD = 0b10000_00000_00000
if __name__ == '__main__':
    N = int(input())
    code = input()

    row = N // 5

    candidate = 0b0

    for i in range(row):
        column = 0
        for j in range(5):
            if code[j * row + i] == '#':
                column = (column << 1) + 1
            else:
                column = column << 1

        if (not column and candidate ^ NUMS[1] == 0) or \
                (i == row - 1 and candidate == 0 and column ^ NUMS[1] == 0):
            print(1, end='')

        # If whole column is empty
        if not column:
            candidate = 0
        else:
            candidate = (candidate << 5) + column

        if candidate & THRESHOLD == THRESHOLD:
            for idx, num in enumerate(NUMS):
                if num ^ candidate == 0:
                    print(idx, end='')
                    candidate = 0
                    break
