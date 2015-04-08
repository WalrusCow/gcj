import sys
import operator as op
from functools import reduce

def test():
    n = int(sys.stdin.readline())
    lines = []
    numInt = 0
    for _ in range(n):
        lines.append([int(x) for x in sys.stdin.readline().split()])

    for _ in range(n):
        # Current line we are working with
        l = lines.pop()

        # We need start on one side and end on the other
        # i.e. the product of the subtractions must be negative...
        for ln in lines:
            if reduce(op.mul, [op.sub(*i) for i in zip(l, ln)]) < 0:
                numInt += 1

    return numInt

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)


