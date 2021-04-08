def snakematrix(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            for j in range(len(arr)):
                print(arr[i][j], end=" ")
        else:
            for j in range(len(arr)-1, -1, -1):
                print(arr[i][j], end=" ")
if __name__ == '__main__':
    arr = [[10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]]
    snakematrix(arr)





