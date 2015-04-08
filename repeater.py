import sys

def countLetters(word):
    ''' Count consecutive letter strings in a word.
    Return a list of tuples (letter, number).
    '''

    last = word[0]
    n = 0
    l = []
    for c in word:
        if c == last:
            n += 1
        else:
            l.append((last, n))
            last = c
            n = 1
    l.append((last, n))
    return l

def test():
    ''' Do one test case. '''

    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(n)]

    # For each word we must find the unique letters in a row, and their
    # counts
    # Then we must find the median value, and for each one... add the distance

    counts = []
    letterLen = None
    for w in words:
        c = countLetters(w)
        if letterLen is None: letterLen = len(c)
        if len(c) != letterLen:
            return 'Fegla Won'
        counts.append(c)

    moves = 0

    # Now each one has the same length, guaranteed
    for lcount in zip(*counts):
        # Sort by counts
        lcount = sorted(lcount, key=lambda x: x[1])
        # Get the median count
        median = med(lcount)
        # Now go through each letter, one by one
        ltr = lcount[0][0]
        for c in lcount:
            # Ensure that all are the same letter
            if c[0] != ltr: return 'Fegla Won'
            # Add distance to median (either add or remove letter)
            moves += abs(c[1] - median)
    return moves

def med(lst):
    l = len(lst)
    if l % 2 == 1:
        # Odd - middle element
        return lst[l//2][1]
    # Even - average of middle elements
    return (lst[l//2][1] + lst[l//2 - 1][1]) // 2

def main(n):
    ''' Read and perform n test cases. '''

    for i in range(n):
        answer = test()
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    main(n)


