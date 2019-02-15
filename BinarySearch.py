#requires sorted list and key to search for
def binarySearch(sortedList, key):

    middle = (len(sortedList) - 1)//2
    left = 0
    right = len(sortedList)
    while key != sortedList[middle] and left < right:
        if key < sortedList[middle]:
            right = middle - 1
            middle = (left + right) // 2
        else:
            left = middle + 1
            middle = (left + right) // 2
    if key == sortedList[middle]:
        return middle

    else:
        return False


def main():
    listToSearch = [2, 6, 7, 9, 12, 13, 15, 17, 18, 21, 24, 29, 32, 35]
    keyToFind = 9

    print(binarySearch(listToSearch, keyToFind))

if __name__ == "__main__":
    main()