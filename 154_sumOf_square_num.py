# Sum of Square Numbers

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c**0.5)
        
        while l <= r:
            SquareSum = l*l + r*r
            if SquareSum == c:
                return True
            elif SquareSum < c:
                l += 1
            else:
                r -= 1
        return False