def validMountainArray(A):
    if len(A) < 3 or A[0] >= A[1]:
        return False

    downhill = False

    for i in range(1, len(A)):
        if not downhill:
            if A[i - 1] >= A[i]:
                downhill = True
        if downhill:
            if A[i - 1] <= A[i]:
                return False
    return downhill

if __name__ == '__main__':
    A = [0,2,3,1,0]
    print(validMountainArray(A))