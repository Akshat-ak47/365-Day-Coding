# Greatest-common-divisor-of-strings

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        length = gcd(len(str1), len(str2))
        return str1[:length]

solution = Solution()
str_1 = "ABCABCABC"
str_2 = "ABC"

print(solution.gcdOfStrings(str_1, str_2))