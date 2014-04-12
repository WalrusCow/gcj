import sys

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)

