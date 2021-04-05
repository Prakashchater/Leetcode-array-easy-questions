arr = [400]
l = [0]*len(arr)
maxtemp = -1
if len(arr) == 1:
    arr[0] = -1
for i in range(len(arr)-1,-1,-1):
    temp = arr[i]
    arr[i] = maxtemp
    maxtemp = max(temp,maxtemp)
print(arr)

#
# def solution(arr):
#     if len(arr) == 1:  # If only 1 element replace it with -1
#         arr[0] = -1
#         return arr
#
#     idx = len(arr) - 1  # Starting from right side keeping track of max value
#
#     currmax = arr[idx]
#     arr[idx] = -1  # Handling edge case - last element = -1
#
#     idx -= 1  # Starting from second last element
#
#     while idx >= 0:
#         temp = arr[idx]  # Store current element before replacing with max
#         arr[idx] = currmax
#
#         if temp > currmax:  # Find the max value for next iteration
#             currmax = temp
#
#         idx -= 1
#
#     return arr
#
# arr = [17,18,4,5,6,1]
# print(solution(arr))
