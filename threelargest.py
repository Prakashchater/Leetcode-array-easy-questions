def largest(arr):
    threelargest = [None, None, None]
    for num in arr:
        updateLargest(threelargest, num)
    return threelargest

def updateLargest(threelargest, num):
    if threelargest[2] == None or num > threelargest[2]:
        shiftandUpdate(threelargest, num, 2)
    elif threelargest[2] == None or num > threelargest[2]:
        shiftandUpdate(threelargest, num, 1)
    elif threelargest[2] == None or num > threelargest[2]:
        shiftandUpdate(threelargest, num, 1)

def shiftandUpdate(arr, num, idx):
    for i in range(idx + 1):
        if i == idx:
            arr[i] = num
        else:
            arr[i] = arr[i + 1]

if __name__ == '__main__':
    arr = [10, 4, 3, 50, 23, 90]
    print(largest(arr))
