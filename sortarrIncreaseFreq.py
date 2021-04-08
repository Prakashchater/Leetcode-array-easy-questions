from collections import defaultdict
arr = [1,1,2,2,2,3]
count = defaultdict(int)
for i in arr:
    count[i] += 1
# print(count)
freq = sorted([(key,val) for key,val in count.items()], key=lambda x: (x[1],-x[0]))
print(freq)
f = []
for e in freq:
    f += [e[0]]
print(f)
