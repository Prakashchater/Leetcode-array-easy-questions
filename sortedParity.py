# def solution(arr):
#     even = 0
#     odd = 1
#     res = [0]*len(arr)
#     for i in range(len(arr)):
#         if arr[i] % 2 == 0:
#             res[even] = arr[i]
#             even += 2
#         elif arr[i] % 2 != 0:
#             res[odd] = arr[i]
#             odd += 2
#     return res
#
# if __name__ == '__main__':
#     arr = [5,2,1,8]
#     print(solution(arr))



# def candy(candies, extraCandies):
#     c = []
#     l = []
#     max_can = max(candies)
#     for can in candies:
#         can += extraCandies
#         if can > max_can:
#             can = max_can
#         c.append(can)
#     for i in c:
#         if i == max_can:
#             l.append(True)
#         else:
#             l.append(False)
#     return l
#
#
# if __name__ == '__main__':
#     candies = [2,3,5,1,3]
#     extraCandies = 3
#     print(candy(candies, extraCandies))

#
# arr = [2, 1, 4, 3]
# index = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         arr[i], arr[index] = arr[index], arr[i]
#         index += 1
# print(arr)


# Part 2
"""
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""
arr = [4,2,5,7]
j = 1
for i in range(0, len(arr), 2):
    if arr[i] % 2 :
        while arr[j] % 2:
            j += 2
        arr[i], arr[j] = arr[j], arr[i]
print(arr)








