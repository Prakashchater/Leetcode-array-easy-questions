# n = 4
# k = n*2-2
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i+1):
#         print("#", end=" ")
#     print("\r")


# arr = [7, 69, 2, 221, 8974]
# arr.sort()
# print(arr)
# a = sum(arr[0:len(arr)-1])
# print(a)
# b = sum(arr[1:len(arr)])
# print(b)


##Time conversion

# def time(s):
#     if s[-2:] == "AM" and s[:2] == "12":
#         return "00" + s[2:-2]
#     elif s[-2:] == "AM":
#         return s[:-2]
#     elif s[-2:] == "PM" and s[:2] == "12":
#         return s[:2]
#     else:
#         return str(int(s[:2]) + 12) + s[2:8]
#
# if __name__ == '__main__':
#     s = "12:05:45AM"
#     print(time(s))


def grading(grades):
    # Write your code here
    res = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5
            # print(mod5)
            if mod5 >= 3:
                grade += (5 - mod5)
        res.append(grade)
    return res

grades = [73, 67, 38, 33]
print(grading(grades))
