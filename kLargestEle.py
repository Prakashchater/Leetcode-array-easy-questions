def Klargest(arr,k):
    arr.sort()
    for i in range(len(arr)):
        arr[:] = arr[:-k]
    return arr

if __name__ == '__main__':
    arr = [12, 5, 787, 1, 23]
    k = 2
    print(Klargest(arr,k))