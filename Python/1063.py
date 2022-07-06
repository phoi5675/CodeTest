
VEC = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1),
}
MAP_SIZE = 8

if __name__ == '__main__':
    def convert_to_yx(coord: str) -> tuple:
        y = int(coord[1])
        x = ord(coord[0]) - ord('A') + 1
        return y, x

    def convert_to_chess(y: int, x: int) -> str:
        return chr(ord('A') + x - 1) + str(y)

    king, pawn, N = list(map(str, input().split()))
    N = int(N)
    moves = []
    for _ in range(N):
        moves.append(input())

    for move in moves:
        k_ty, k_tx = convert_to_yx(king)
        p_ty, p_tx = convert_to_yx(pawn)

        dy, dx = VEC[move]
        if 1 <= k_ty + dy <= 8 and 1 <= k_tx + dx <= 8:
            # If pawn is in the way and can move
            if (k_ty + dy == p_ty and k_tx + dx == p_tx) \
                    and (1 <= p_ty + dy <= 8 and 1 <= p_tx + dx <= 8):
                king = convert_to_chess(k_ty + dy, k_tx + dx)
                pawn = convert_to_chess(p_ty + dy, p_tx + dx)
            # If pawn is not in the way
            if k_ty + dy != p_ty or k_tx + dx != p_tx:
                king = convert_to_chess(k_ty + dy, k_tx + dx)

    print(king)
    print(pawn)
