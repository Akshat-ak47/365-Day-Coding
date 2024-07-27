# Strictly Palindromic Number

# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
# Given an integer n, return true if n is strictly palindromic and false otherwise.
# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: n = 9
# Output: false
# Explanation: In base 2: 9 = 1001 (base 2), which is palindromic.
# In base 3: 9 = 100 (base 3), which is not palindromic.
# Therefore, 9 is not strictly palindromic so we return false.

class Solution:
    def is_palindrome(self, n, base):
        if n == 0:
            return True

        digits = []
        while (n > 0):
            digits.append(n % base)
            n //= base
        
        return digits == digits[::-1]

    def isStrictlyPalindromic(self, n: int) -> bool:
        if n < 2:
            return False
        
        for base in range(2, n-1):
            if not self.is_palindrome(n, base):
                return False
        
        return True
    
    