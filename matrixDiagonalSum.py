def matrix(arr):
    row = len(arr)
    col = row
    count = 0
    for i in range(row):
        for j in range(col):
            if i == j or i+j == len(arr)-1:
                count+=arr[i][j]
    return count

if __name__ == '__main__':
    arr = [[1,2,1],[1,1,1],[1,1,1]]
    print(matrix(arr))