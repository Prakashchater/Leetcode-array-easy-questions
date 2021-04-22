arr = [1,2,2,6,6,6,6,7,10]
d = {}
for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

for key, val in d.items():
    print(key,":",val)