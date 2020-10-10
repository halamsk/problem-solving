#https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Follow up: Could you solve it without converting the integer to a string?
#
#
#
# Example 1:
#
# Input: x = 121
# Output: true
#
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Example 4:
#
# Input: x = -101
# Output: false
#
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
#



class Solution:



#Solution 1: This solution is a by reversing the number and then check if its same or not. the complexity will be O(n) when n is the input number

#     def isPalindrome(self, x: int) -> bool:
#         if x<0:
#             return False

#         rev = 0
#         temp = x
#         while temp>0:
#             rev = (rev*10)+(temp%10)
#             temp = temp//10
#         return rev == x


# Solution 2: This solution does not completely reverse the number as we don't need to because we don't need to check the whole number so it splits the
#             number. For odd digits number we can discard the middle digit as it will be in the middle in both the numbers(original and reverse).
#             This will have O(log n) when n is the input number and log is of base 10

def isPalindrome(self, x: int) -> bool:
    if x<0 or (x%10==0 and x!=0):
        return False
    rev = 0
    while x>rev:
        rev = rev*10 + x%10
        x //= 10
    return x==rev or x==rev//10
