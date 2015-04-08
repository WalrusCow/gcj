import sys

def test():
    # Read the board
    board = []
    for _ in range(4):
        board.append(sys.stdin.readline().strip())
    sys.stdin.readline()

    def chk(p):
        # Any rows/columns
        search = 'T' + p
        for b in (zip(*board), board):
            if any(all(c in search for c in s) for s in b):
                return True
        # Diagonals
        l = ((s[i] for i, s in enumerate(board)),
             (s[3-i] for i, s in enumerate(board)))
        return any(all(c in search for c in s) for s in l)

    for c in 'OX':
        if chk(c): return c + ' won'

    if any('.' in s for s in board):
        return 'Game has not completed'

    return 'Draw'

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)

