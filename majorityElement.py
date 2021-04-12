def majority_element(nums):
    majority_count = len(nums) // 2
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majority_count:
            return num


if __name__ == '__main__':
    nums = [1,1,2,2,2,1,1]
    print(majority_element(nums))


# l = [1,2,3,4,5,2,3,4,7,9,5]
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i,end=" ")