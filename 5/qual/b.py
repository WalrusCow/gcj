import sys
import math
from collections import Counter
from operator import itemgetter

def test():
    # l of n value => ceil(n/2) + l moves after split
    sys.stdin.readline()
    nums = map(int, sys.stdin.readline().strip().split())
    # Sort by number of cakes. Also count how many of each number there are
    # cakeCounts is a list of (n, l) for l piles of n cakes high
    cakeCounts = Counter(nums)

    moves = 0
    while cakeCounts:
        count = max(cakeCounts.keys())
        piles = cakeCounts[count]

        frac = count / 2
        ceil, floor = math.ceil(frac), math.floor(frac)
        if ceil + piles < count:
            # We should divide these in half
            cakeCounts[ceil] += piles
            cakeCounts[floor] += piles
            moves += piles
            del cakeCounts[count]
        else:
            moves += count
            break
    return moves


def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)

