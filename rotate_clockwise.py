# def rotate(arr):
#
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

def rotation(arr,d,n):
    for i in range(0,d):
        temp = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = list(map(int,input().split()))
        n = a[0]
        d = a[1]
        arr = list(map(int,input().split()))
        print(rotation(arr, d, n))

    # [29, 42, 51, 94, 1, 35, 65, 25, 40, 13, 27, 87, 95, 40, 96, 71, 35, 79, 68, 2, 98, 3, 18, 93, 53, 57, 2, 81, 87, 42,
    #  66, 90, 45, 20, 41, 30, 32, 18, 98, 72, 82, 76, 10, 28, 68, 57, 98, 54, 87, 66, 7, 84, 20, 25, 29, 72, 33, 30, 4,
    #  20, 71, 69, 9, 16, 41, 50, 97, 24, 19, 46, 47, 52, 22, 56, 80, 89, 65]