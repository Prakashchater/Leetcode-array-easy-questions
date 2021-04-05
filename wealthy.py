# def maximumWealth(accounts):
#     l = []
#     for i in range(len(accounts)):
#         t = sum(accounts[i])
#         l.append(t)
#     return max(l)
#
# if __name__ == '__main__':
#     accounts = [[1,2,3],[4,5,6]]
#     print(maximumWealth(accounts))

# def smallerNumbersThanCurrent(nums):
#     out = []
#     n = sorted(nums)
#     for i in nums:
#         out.append(n.index(i))
#     return out
#
#     # for i in range(len(nums)):
#     #     num = nums[i]
#     #     count = 0
#     #     for j in range(len(nums)):
#     #         if nums[j] < num:
#     #             count += 1
#     #     out.append(count)
#     # return out
#
# if __name__ == '__main__':
#     nums = [8,1,2,2,3]
#     print(smallerNumbersThanCurrent(nums))

import math
n = 5
out = []
for i in range(1,n+1):
    y = math.floor(n/i)
    out.append(i*y)
print(sum(out))
