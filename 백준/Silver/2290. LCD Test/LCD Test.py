SEG_7 = {
    '0': 0b011_1111,
    '1': 0b000_0110,
    '2': 0b101_1011,
    '3': 0b100_1111,
    '4': 0b110_0110,
    '5': 0b110_1101,
    '6': 0b111_1101,
    '7': 0b000_0111,
    '8': 0b111_1111,
    '9': 0b110_1111,
}
if __name__ == '__main__':
    s, n = input().split()
    s = int(s)
    width, height = s + 2, s * 2 + 3

    for y in range(height):
        for num in n:
            if y == 0:
                if SEG_7[num] & 0b1 == 0b1:
                    print(f' {"-" * s} ', end=' ')
                else:
                    print(f' {" " * s} ', end=' ')
            elif 0 < y < (2 * s + 3) // 2:
                if SEG_7[num] & 0b010_0000 == 0b010_0000:
                    print('|', end='')
                else:
                    print(' ', end='')

                print(f'{" " * (width - 2)}', end='')

                if SEG_7[num] & 0b000_0010 == 0b000_0010:
                    print('|', end='')
                else:
                    print(' ', end='')
                print(' ', end='')
            elif y == (2 * s + 3) // 2:
                if SEG_7[num] & 0b100_0000 == 0b100_0000:
                    print(f' {"-" * s} ', end=' ')
                else:
                    print(f' {" " * s} ', end=' ')
            elif y == (2 * s + 3 - 1):
                if SEG_7[num] & 0b000_1000 == 0b000_1000:
                    print(f' {"-" * s} ', end=' ')
                else:
                    print(f' {" " * s} ', end=' ')
            elif (2 * s + 3) // 2 < y < 2 * s + 3 - 1:
                if SEG_7[num] & 0b001_0000 == 0b001_0000:
                    print('|', end='')
                else:
                    print(' ', end='')

                print(f'{" " * (width - 2)}', end='')

                if SEG_7[num] & 0b000_0100 == 0b000_0100:
                    print('|', end='')
                else:
                    print(' ', end='')
                print(' ', end='')

        print()
