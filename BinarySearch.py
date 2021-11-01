def binarySearch(inputArray, value):
    high = len(inputArray) - 1
    low = 0

    found = False
    loc = -1

    while(found != True):
        if(high < low):
            return -1

        mid = low + (high - low) // 2

        if(inputArray[mid] < value):
            low = mid + 1

        if(inputArray[mid] > value):
            high = mid - 1

        if(inputArray[mid] == value):
            return mid

i = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print(binarySearch(i, 13))
