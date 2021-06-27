def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    smallest = float("inf")
    curr = float("inf")
    smallestPair = []
    while i < len(arr1) and j < len(arr2):
        firstNum = arr1[i]
        secondNum = arr2[j]
        if firstNum < secondNum:
            curr = abs(firstNum - secondNum)
            i += 1
        elif firstNum > secondNum:
            curr = abs(firstNum - secondNum)
            j += 1
        else:
            return [firstNum, secondNum]

        if smallest > curr:
            smallest = curr
            smallestPair = [firstNum, secondNum]
    return smallestPair

if __name__ == '__main__':
    arr1 = [-1, 5, 10, 20, 28, 3]
    arr2 = [26, 134, 135, 15, 17]
    print(smallestDifference(arr1, arr2))


