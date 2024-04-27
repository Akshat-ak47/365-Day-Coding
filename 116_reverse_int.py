# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
            x = abs(x)
        
        x = str(x)
        digits = x[1:] if sign==-1 else x

        reverse_digit = x[::-1]
        reversed_x = int(reverse_digit) * sign

        if reversed_x < -2**31 or reversed_x > 2**31:
            return 0
        else:
            return reversed_x


solution = Solution()
print(solution.reverse(123))
