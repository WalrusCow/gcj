import sys
from functools import reduce

def test():
    ''' Return n, barber for hair cutting. '''
    _, position = map(int, sys.stdin.readline().strip().split())
    barbers = list(map(int, sys.stdin.readline().strip().split()))

    if position <= len(barbers):
        return position

    times = barbers[:]
    position -= len(times)
    position %= reduce(lambda x, y: x * y, barbers, 1)

    while position > 0:
        m = min(times)
        for i, t in enumerate(times):
            t -= m
            if t == 0:
                times[i] = barbers[i]
                position -= 1
                if position <= 0:
                    return i+1
            else:
                times[i] = t
    return i

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)
