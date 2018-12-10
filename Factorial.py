

#calculates n recursively
def factorialRecur(n):

    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorialRecur(n - 1) * n

#calculates n iteratively
def factorialIter(n):
    returnVal = 1
    for i in range(1, n + 1):
        returnVal = returnVal * i
    return returnVal

def main():
    print(factorialRecur(5))
    print(factorialIter(5))

if __name__ == "__main__":
    main()