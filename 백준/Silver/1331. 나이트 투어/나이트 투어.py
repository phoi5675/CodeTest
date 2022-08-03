from typing import *

VEC = ((-2, 1), (-2, -1), (1, -2), (-1, -2), (2, 1), (2, -1), (1, 2), (-1, 2))

if __name__ == '__main__':
    tours: List[Tuple[int, int]] = []
    visit_checker: List[List[bool]] = [[False] * 6 for _ in range(6)]
    for _ in range(36):
        x, y = list(input())
        converted_x: int = ord(x) - ord('A')
        if visit_checker[int(y) - 1][converted_x]:
            print("Invalid")
            exit(0)
        tours.append((int(y), converted_x))
        visit_checker[int(y) - 1][converted_x] = True

    for i in range(36 - 1):
        cur_y, cur_x = tours[i]
        next_y, next_x = tours[i + 1]
        is_valid: bool = False

        for dy, dx in VEC:
            if next_y == cur_y + dy and next_x == cur_x + dx:
                is_valid = True
                break

        if not is_valid:
            print("Invalid")
            exit(0)

    end_y, end_x = tours[-1]
    start_y, start_x = tours[0]
    for dy, dx in VEC:
        if start_y == end_y + dy and start_x == end_x + dx:
            print("Valid")
            exit(0)

    print("Invalid")
