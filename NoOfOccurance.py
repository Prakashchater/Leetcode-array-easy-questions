def no_occurance(arr,k):
    res = 0
    for i in range(len(arr)):
        if arr[i] == k:
            res += 1
    return res




if __name__ == '__main__':

    arr = [1,1,2,2,2,2,3,4]
    k = 2
    print(no_occurance(arr,k))