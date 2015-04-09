import sys

def test():
    rows, cols = list(map(int, sys.stdin.readline().strip().split()))
    lawn = []
    for _ in range(rows):
        lawn.append(list(map(int, sys.stdin.readline().strip().split())))

    # We have to cut each row/col at the maximum entry in that row/col
    rowCuts = []
    for row in lawn:
        rowCuts.append(max(row))
    colCuts = []
    for col in zip(*lawn):
        colCuts.append(max(col))

    for i, row in enumerate(lawn):
        for j, entry in enumerate(row):
            # If we can't cut either the row or column short enough then
            # this arrangement is not possible
            if rowCuts[i] > entry and colCuts[j] > entry:
                return 'NO'
    return 'YES'


def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)

