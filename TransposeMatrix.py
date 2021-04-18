# def transpose(arr):
#     res = []
#     for i in range(len(arr[0])):
#         temp = []
#         for j in range(len(arr)):
#             temp.append(arr[j][i])
#         res.append(temp)
#     return res
#
# if __name__ == '__main__':
#     arr = [[1,2,3],[4,5,6]]
#     print(transpose(arr))


def addMatrices(x,y):
    l = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(x[0])):
        for j in range(len(y[0])):
            l[i][j] = x[i][j] + y[i][j]
    return l


if __name__ == '__main__':
    x = [[1,2,1],
    [4 ,5,6],
    [7 ,8,9]]
    y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
    print(addMatrices(x,y))