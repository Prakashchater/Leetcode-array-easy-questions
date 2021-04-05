def students(arr1, arr2):
    c = 0
    while arr1 and arr2:
        if arr1[0] == arr2[0]:
            arr1.pop(0)
            arr2.pop(0)
            c = 0
        else:
            temp = arr1.pop(0)
            c += 1
            arr1.append(temp)
            if c > len(arr1):
                return len(arr1)
    return 0

if __name__ == '__main__':
    arr1 = [1, 0, 0, 1]
    arr2 = [0, 1, 0, 1]
    print(students(arr1,arr2))