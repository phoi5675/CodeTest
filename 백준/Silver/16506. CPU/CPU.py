import sys

OP = {
    'ADD': 0b0000,
    'SUB': 0b0001,
    'MOV': 0b0010,
    'AND': 0b0011,
    'OR': 0b0100,
    'NOT': 0b0101,
    'MULT': 0b0110,
    'LSFTL': 0b0111,
    'LSFTR': 0b1000,
    'ASFTR': 0b1001,
    'RL': 0b1010,
    'RR': 0b1011,
}

RD, RA, RB = 0, 1, 2
if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        op = sys.stdin.readline().split()
        regs = list(map(int, op[1:]))

        is_constant = True if op[0][-1] == 'C' else False
        opcode = op[0] if not is_constant else op[0][0:-1]
        r_b = regs[RB] if is_constant else regs[RB] << 1
        print(f'{OP[opcode]:0>4b}'
              f'{1 if is_constant else 0}'
              f'0'
              f'{regs[RD]:0>3b}'
              f'{regs[RA]:0>3b}'
              f'{r_b:0>4b}')
