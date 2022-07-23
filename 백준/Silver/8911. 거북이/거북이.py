import sys

VEC = ((-1, 0), (0, -1), (1, 0), (0, 1))
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        moves = sys.stdin.readline()
        v = UP
        y, x = 0, 0
        upper_right, down_left = [0, 0], [0, 0]

        for move in moves:
            # Calculate move
            if move == 'F':
                y, x = y + VEC[v][0], x + VEC[v][1]
            elif move == 'B':
                y, x = y + VEC[(v + 2) % 4][0], x + VEC[(v + 2) % 4][1]
            elif move == 'L':
                v = (v + 1) % 4
            elif move == 'R':
                v = (v - 1) % 4 if 0 <= (v - 1) % 4 < 4 else 3

            # Update rectangle coordinate
            upper_right = max(upper_right[0], y), max(upper_right[1], x)
            down_left = min(down_left[0], y), min(down_left[1], x)

        print(abs(upper_right[0] - down_left[0]) * abs(upper_right[1] - down_left[1]))
