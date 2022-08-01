from typing import *
from copy import deepcopy

TOP, FRONT, BOTTOM, BACK, LEFT, RIGHT = 0, 1, 2, 3, 4, 5
PLANES = {'U': TOP, 'F': FRONT, 'D': BOTTOM, 'B': BACK, 'L': LEFT, 'R': RIGHT}
COLORS = ('w', 'r', 'y', 'o', 'g', 'b')

if __name__ == '__main__':
    def rotate(area: int, is_clockwise: bool) -> None:
        tmp: List[List[str]] = [[''] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    tmp[i][j] = cube[area][i][j]
                if is_clockwise:
                    tmp[i][j] = cube[area][3 - (j + 1)][i]
                else:
                    tmp[i][j] = cube[area][j][3 - (i + 1)]
        cube[area] = deepcopy(tmp)

    n = int(input())
    cube: List[List[List[str]]] = []

    for color in COLORS:
        cube.append([[color] * 3 for _ in range(3)])

    original_cube = deepcopy(cube)

    for _ in range(n):
        rotations: int = int(input())
        commands: List[str] = input().split()
        cube = deepcopy(original_cube)
        for command in commands:
            is_clockwise: bool = True if command[1] == '+' else False
            plane: str = command[0]
            rotate(PLANES[plane], is_clockwise)

            for i in range(3):
                if plane == 'U':
                    if is_clockwise:
                        cube[FRONT][0][i], cube[RIGHT][0][i], cube[BACK][0][i], cube[LEFT][0][i] = \
                            cube[RIGHT][0][i], cube[BACK][0][i], cube[LEFT][0][i], cube[FRONT][0][i]
                    else:
                        cube[FRONT][0][i], cube[RIGHT][0][i], cube[BACK][0][i], cube[LEFT][0][i] = \
                            cube[LEFT][0][i], cube[FRONT][0][i], cube[RIGHT][0][i], cube[BACK][0][i]
                elif plane == 'D':
                    if is_clockwise:
                        cube[FRONT][2][i], cube[RIGHT][2][i], cube[BACK][2][i], cube[LEFT][2][i] = \
                            cube[LEFT][2][i], cube[FRONT][2][i], cube[RIGHT][2][i], cube[BACK][2][i]
                    else:
                        cube[FRONT][2][i], cube[RIGHT][2][i], cube[BACK][2][i], cube[LEFT][2][i] = \
                            cube[RIGHT][2][i], cube[BACK][2][i], cube[LEFT][2][i], cube[FRONT][2][i]
                elif plane == 'F':
                    if is_clockwise:
                        cube[TOP][2][i], cube[RIGHT][i][0], cube[BOTTOM][0][-(i + 1)], cube[LEFT][-(i + 1)][2] = \
                            cube[LEFT][-(i + 1)][2], cube[TOP][2][i], cube[RIGHT][i][0], cube[BOTTOM][0][-(i + 1)]
                    else:
                        cube[TOP][2][i], cube[RIGHT][i][0], cube[BOTTOM][0][-(i + 1)], cube[LEFT][-(i + 1)][2] = \
                            cube[RIGHT][i][0], cube[BOTTOM][0][-(i + 1)], cube[LEFT][-(i + 1)][2], cube[TOP][2][i]
                elif plane == 'B':
                    if is_clockwise:
                        cube[TOP][0][i], cube[LEFT][-(i + 1)][0], cube[BOTTOM][2][-(i + 1)], cube[RIGHT][i][2] = \
                            cube[RIGHT][i][2], cube[TOP][0][i], cube[LEFT][-(i + 1)][0], cube[BOTTOM][2][-(i + 1)]
                    else:
                        cube[TOP][0][i], cube[LEFT][-(i + 1)][0], cube[BOTTOM][2][-(i + 1)], cube[RIGHT][i][2] = \
                            cube[LEFT][-(i + 1)][0], cube[BOTTOM][2][-(i + 1)], cube[RIGHT][i][2], cube[TOP][0][i]
                elif plane == 'L':
                    if is_clockwise:
                        cube[TOP][i][0], cube[FRONT][i][0], cube[BOTTOM][i][0], cube[BACK][-(i + 1)][2] = \
                            cube[BACK][-(i + 1)][2], cube[TOP][i][0], cube[FRONT][i][0], cube[BOTTOM][i][0]
                    else:
                        cube[TOP][i][0], cube[FRONT][i][0], cube[BOTTOM][i][0], cube[BACK][-(i + 1)][2] = \
                            cube[FRONT][i][0], cube[BOTTOM][i][0], cube[BACK][-(i + 1)][2], cube[TOP][i][0]
                elif plane == 'R':
                    if is_clockwise:
                        cube[TOP][i][2], cube[FRONT][i][2], cube[BOTTOM][i][2], cube[BACK][-(i + 1)][0] = \
                            cube[FRONT][i][2], cube[BOTTOM][i][2], cube[BACK][-(i + 1)][0], cube[TOP][i][2]
                    else:
                        cube[TOP][i][2], cube[FRONT][i][2], cube[BOTTOM][i][2], cube[BACK][-(i + 1)][0] = \
                            cube[BACK][-(i + 1)][0], cube[TOP][i][2], cube[FRONT][i][2], cube[BOTTOM][i][2]

        for i in range(3):
            print(''.join(cube[TOP][i]))
