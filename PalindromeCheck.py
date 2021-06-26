# Time: O(N)      Space:O(1)
def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    s = 'malayalam'
    print(isPalindrome(s))


# Time: O(N)      Space:O(N)
"""
# def isPalindrome(s, i=0):
#     j = len(s) - 1 - i
#     return True if i >= j else s[i] == s[j] and isPalindrome(s, i + 1)
#
# if __name__ == '__main__':
#     s = 'abcdcbaw'
#     print(isPalindrome(s))
    
def isPalindrome(s, i=0):
    j = len(s) - 1 - i
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return isPalindrome(s, i + 1)

if __name__ == '__main__':
    s = 'abcdcbaw'
    print(isPalindrome(s))
"""

# Time : O(N^2)       Space: O(N)
"""
def palindrome(string):
    reverseString = ""
    for i in reversed(range(len(string))):
        reverseString += string[i]
    return string == reverseString

if __name__ == '__main__':
    string = 'abcdcba'
    print(palindrome(string))
"""

# Time: O(N)      Space: O(N)
"""
def isPalindrome(s):
    reverseString = []
    for i in reversed(range(len(s))):
        reverseString.append(s[i])
    return s == ''.join(reverseString)

if __name__ == '__main__':
    s = 'malayalam'
    print(isPalindrome(s))
"""
