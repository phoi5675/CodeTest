from typing import *
from collections import deque

VEC = ((-1, 0), (0, -1), (1, 0), (0, 1))
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
EMPTY, SNAKE, APPLE = 0, 1, 2


class Snake:
    def __init__(self):
        self.trail: Deque[Tuple[int, int]] = deque()
        self.direction: int = RIGHT
        self.head: List[int] = [0, 0]

        self.trail.append((self.head[0], self.head[1]))

    def move(self, dy: int, dx: int) -> None:
        self.head[0] += dy
        self.head[1] += dx

        self.trail.append((self.head[0], self.head[1]))

    def change_direction(self, direction: str) -> None:
        if direction == 'D':
            self.direction = self.direction - 1 if self.direction > 0 else len(VEC) - 1
        elif direction == 'L':
            self.direction = (self.direction + 1) % len(VEC)


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    board: List[List[int]] = [[0] * N for _ in range(N)]
    board[0][0] = SNAKE
    snake = Snake()
    elapsed: int = 0
    is_game_over: bool = False
    move_commands: Deque[Tuple[int, str]] = deque()

    for _ in range(K):
        y, x = list(map(int, input().split()))
        board[y - 1][x - 1] = APPLE

    L = int(input())
    for _ in range(L):
        time, curve_to = input().split()
        move_commands.append((int(time), curve_to))

    while not is_game_over:
        # Tik-tok
        elapsed += 1

        # Move snake
        snake.move(*VEC[snake.direction])

        # Check glitch
        if snake.head[0] < 0 or snake.head[0] >= N or \
                snake.head[1] < 0 or snake.head[1] >= N:
            is_game_over = True
            break

        on_board: int = board[snake.head[0]][snake.head[1]]
        # Check board where head is going to be in
        if on_board == SNAKE:
            is_game_over = True
            break
        # Eat apple
        elif on_board != APPLE:
            tail_y, tail_x = snake.trail.popleft()
            board[tail_y][tail_x] = EMPTY
        board[snake.head[0]][snake.head[1]] = SNAKE

        # Check whether snake is changing its heading
        if move_commands and elapsed == move_commands[0][0]:
            _, direc = move_commands.popleft()
            snake.change_direction(direc)

    print(elapsed)
