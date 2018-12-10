
#finds the nth Fibonacci number iteratively
def fibSeqIter(n):
    
    twoPrev = 0
    onePrev = 1
    curr = 0
    for i in range(1, n):
        curr = twoPrev + onePrev
        twoPrev = onePrev
        onePrev = curr
    return curr

#finds the nth Fibonacci number recursively
def fibSeqRecur(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibSeqRecur(n - 1) + fibSeqRecur(n - 2)

def main():
    print(fibSeqIter(7))
    print(fibSeqRecur(7))

if __name__ == "__main__":
    main()