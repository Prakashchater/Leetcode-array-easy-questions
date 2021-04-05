# arr = [1,4,3,2]
# arr.sort()
# count = 0
# for i in range(0,len(arr),2):
#     count += arr[i]
# print(count)

arr = [-4,-1,0,3,10]
l = []
for i in arr:
    temp = i*i
    l.append(temp)
print(sorted(l))
