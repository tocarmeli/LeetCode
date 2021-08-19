# https://leetcode.com/problems/palindrome-number/
# Question 9: Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        concatenatedNum = str(x)
        palindrome = concatenatedNum[::-1]

        if (palindrome == concatenatedNum):
            return True
        return False


test = Solution()
print(test.isPalindrome(10))