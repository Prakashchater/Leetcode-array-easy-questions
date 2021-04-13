def operations():
    global output
    ol = input().split()
    operation = ol[0]
    update_set = set(map(int, input().split()))
    if operation == "intersection_update":
        a.intersection_update(update_set)
    elif operation == "update":
        a.update(update_set)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(update_set)
    elif operation == "difference_update":
        a.difference_update(update_set)
    output = sum(a)


input()
a = set(map(int, input().split()))
n = int(input())
for i in range(n):
    operations()
print(output)