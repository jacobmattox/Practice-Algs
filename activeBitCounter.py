#counts number of active bits in the binary representation of the integer n

def countActiveBits(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    print(count)

def main():

    countActiveBits(3)
    countActiveBits(15)
    countActiveBits(255)

if __name__ == "__main__":
    main()