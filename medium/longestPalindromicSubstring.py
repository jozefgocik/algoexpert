# Solution 1
# def longestPalindromicSubstring(string):
#     # O(n ^ 3) time / O(n) space
#     result = ""
#
#     for i in range(len(string)):
#         for j in range(i + 1, len(string) + 1):
#             currentString = string[i:j]
#             if isPalindrome(currentString):
#                 if len(currentString) > len(result):
#                     result = currentString
#
#     return result
#
# def isPalindrome(string):
#     if string == string[::-1]:
#         return True
#
#     return False

# Solution 2
def longestPalindromicSubstring(string):
    # O(n ^ 2) time / O(n) space
    result = ""

    for i in range(len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i, i + 1)
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even

    return result

def getLongestPalindromeFrom(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break

        left -= 1
        right += 1

    return string[left + 1:right]


print(longestPalindromicSubstring("abaxyzzyxf"))
