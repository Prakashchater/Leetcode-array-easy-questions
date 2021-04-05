# def grid(arr):
#     count = 0
#     for i in arr:
#         for j in i:
#             if j < 0:
#                 count += 1
#     return count
#
#
# if __name__ == '__main__':
#     arr = [[4,3,2,-1],[-3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#     print(grid(arr))

arr = [1,2,3,2]
temp = 0
for i in arr:
    if arr.count(i) > 1:
        temp =+ i
print(sum(arr)-temp)