def transpose(arr):
    res = []
    for i in range(len(arr[0])):
        temp = []
        for j in range(len(arr)):
            temp.append(arr[j][i])
        res.append(temp)
    return res

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6]]
    print(transpose(arr))
