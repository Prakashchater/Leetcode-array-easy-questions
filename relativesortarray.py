arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
tail = sorted([i for i in arr1 if i not in arr2])
# print(tail)
l = []
for i in arr2:
    c = arr1.count(i)
    # print(c)
    l += [i] * c
print(l + tail)