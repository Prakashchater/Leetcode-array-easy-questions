# Python3 implementation to find the
# longest subarray consisting of
# only two values with difference K

# Function to return the length
# of the longest sub-array
def longestSubarray(arr, n, k):
    Max = 1

    # Initialize set
    s = set()

    for i in range(n - 1):

        # Store 1st element of
        # sub-array into set
        s.add(arr[i])

        for j in range(i + 1, n):

            # Check absolute difference
            # between two elements
            if (abs(arr[i] - arr[j]) == 0 or
                    abs(arr[i] - arr[j]) == k):

                # If the new element is not
                # present in the set
                if (not arr[j] in s):

                    # If the set contains
                    # two elements
                    if (len(s) == 2):
                        break

                    # Otherwise
                    else:
                        s.add(arr[j])

            else:
                break

        if (len(s) == 2):

            # Update the maximum length
            Max = max(Max, j - i)

            # Remove the set elements
            s.clear()

        else:
            s.clear()

    return Max


# Driver Code
if __name__ == '__main__':

    arr = [1, 1, 1, 2, 2, 3, 3]

    N = len(arr)
    K = 1

    length = longestSubarray(arr, N, K)

    if (length == 1):
        print("-1")
    else:
        print(length)

# This code is contributed by himanshu77
