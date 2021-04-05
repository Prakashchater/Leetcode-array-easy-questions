# arr = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#
# count = 0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i == j or i+j == len(arr)-1:
#             count += arr[i][j]
# print(count)

#Final Prices With a Special Discount in a Shop
arr = [8,4,6,2,3]
l = [-1]*len(arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] >= arr[j]:
            l[i] = arr[i] - arr[j]
            break
    if l[i] == -1:
        l[i] = arr[i]
print(l)




