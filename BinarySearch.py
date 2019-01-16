

#requires sorted list and key to search for
def binarySearch(sortedList, key):

    middle = len(sortedList)//2
    if key == sortedList[middle]:
        return True
    elif key > sortedList[middle]:
        return binarySearch(sortedList[middle + 1: ], key)
    else:
        return binarySearch(sortedList[:middle], key)
    return False

def main():
    listToSearch = [2, 6, 7, 9, 12, 13, 15, 17, 18, 21, 24, 29, 32, 35]
    keyToFind = 24

    print(binarySearch(listToSearch, keyToFind))

if __name__ == "__main__":
    main()