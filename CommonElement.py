# Python function to print common elements in three sorted arrays
def findCommon(A, B, C, n1, n2, n3):
    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0

    # Iterate through three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):

        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (A[i] == B[j] and B[j] == C[k]):
            print(A[i])
            i += 1
            j += 1
            k += 1

        # x < y
        elif A[i] < B[j]:
            i += 1

        # y < z
        elif B[j] < C[k]:
            j += 1

        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k += 1


# Driver program to check above function
A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(A)
n2 = len(B)
n3 = len(C)
findCommon(A, B, C, n1, n2, n3)

