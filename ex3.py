arr = [555,901,482,1771]
count = 0
for i in arr:
    if len(str(i))%2 == 0:
        count += 1
print(count)