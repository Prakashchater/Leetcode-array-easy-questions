# arr = [1,2,3,4,5]
# arr1 = [1,2,3,4,5,6,7,8,9]
# c = set(arr)
# d = set(arr1)
# print(c.issubset(d))

# arr = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
# m = arr[0]
# c = 0
# for i in range(1,len(arr)):
#     if arr[i-1] >= arr[i]:
#         c += 1
# print(c)

# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2
# l = []
# for i in range(len(s)):
#     l.append(s[i:i+m])
# print(l)


# def migratoryBirds(arr):
#     # Write your code here
#     l = [0] * len(arr)
#
#     for i in range(len(arr)):
#         l[arr[i]] += 1
#     return l.index(max(l))
#
# arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
# print(migratoryBirds(arr))


# n = int(input())
k = int(input())
bill = list(map(int, input().split()))
b = int(input())
del bill[k]
temp = sum(bill) // 2
if temp != b:
    print(b-temp)
else:
    print("Bon Appetit")









