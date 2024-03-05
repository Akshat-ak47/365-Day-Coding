'''
Colorful Number

For Given Number A, find if it's a COLORFUL number or not.

COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Return 1 if A is a COLORFUL number, else return 0
'''

class Solution:
    def colorful(self, A):
        num = str(A)
        digits = [int(digit) for digit in num]
        products = set()
        
        for i in range(len(digits)):
            product = 1
            for j in range(i, len(digits)):
                product *= digits[j]
                if product in products:
                    return 0
                products.add(product)
        
        return 1
    
solution = Solution()

number = 3245
print(solution.colorful(number))  # Output: 1 (Colorful)

number = 326
print(solution.colorful(number))  # Output: 0 (Not Colorful)