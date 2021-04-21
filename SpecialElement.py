# def special(nums):
#     for i in range(len(nums)):
#         count = 0
#         for j in nums:
#             if j >= i:
#                 count += 1
#         if count == i:
#             return i
#     return -1
#
#
# if __name__ == '__main__':
#     nums = [0, 4, 3, 0, 4]
#     print(special(nums))

def special(nums):
    nums.sort(reverse=True)     #This method is used to sort the array in descending order.

    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2

        if mid < nums[mid]:
            left = mid + 1
        else:
            right = mid
    return -1 if left < len(nums) and left == nums[left] else left



if __name__ == '__main__':
    nums = [0, 4, 3, 4, 0]
    print(special(nums))

