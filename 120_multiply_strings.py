# Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0" or num2 == "0"):
            return "0"
        else:
            return str(int(num1)*int(num2))

solution = Solution()
num1 = 2
num2 = 3
print(solution.multiply(num1, num2))