# def rotate(arr):
#     x = arr[len(arr)-1]
#     for i in range(len(arr)-1,-1,-1):
#         arr[i] = arr[i-1]
#     arr[0] = x
#     print(arr)
#
# if __name__ == '__main__':
#     arr = [1,2,3,4,5]
#     rotate(arr)

# def multiplyleftright(arr,n):
#     global l,r
#     s = len(arr)//2
#     l = sum(arr[0:s])
#     r = sum(arr[s:])
#     print(l*r)
#
#
# if __name__ == '__main__':
#     arr = [1,2,3,4]
#     n = len(arr)
#     multiplyleftright(arr,n)

# def rotate(arr, d, n):
#     temp = []
#     i = 0
#     while (i < d):
#         temp.append(arr[i])
#         i = i + 1
#     i = 0
#     while (d < n):
#         arr[i] = arr[d]
#         i = i + 1
#         d = d + 1
#     arr[:] = arr[: i] + temp
#     return arr
#
# if __name__ == '__main__':
#     for i in range(int(input())):
#         a = list(map(int, input().split()))
#         d = a[1]
#         n = a[0]
#         arr = list(map(int,input().split()))
#         print(rotate(arr,d,n))

def Leftrotation(arr,d,n):
    for i in range(0,d):
        temp = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    d = 2
    n = len(arr)
    print(Leftrotation(arr,d,n))

