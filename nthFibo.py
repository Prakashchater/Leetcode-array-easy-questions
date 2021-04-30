# time: O(2^n)    || space: O(n)
# def nthfibo(n):
#     if n == 1:
#         return 0
#
#     if n == 2:
#         return 1
#     else:
#         return nthfibo(n-1) + nthfibo(n-2)
#
# n = 6
# print(nthfibo(n))


# Time: O(N)  || Space: O(N)
# def nthfib(n, memo={1: 0, 2: 1}):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = nthfib(n-1, memo) + nthfib(n-2, memo)
#         return memo[n]
#
# if __name__ == '__main__':
#     n = 6
#     print(nthfib(n))


# time: O(N)      || SPACE: O(1)
def nthfibo(n):
    twofib = [0,1]
    counter = 3

    while counter <= n:
        next_fib = twofib[0] + twofib[1]
        twofib[0] = twofib[1]
        twofib[1] = next_fib
        counter += 1

    return twofib[1] if n > 1 else twofib[0]

if __name__ == '__main__':
    n = 6
    print(nthfibo(n))

