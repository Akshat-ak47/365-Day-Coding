'''
Square Root of Integer

Given an integer A.
Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.
'''
class Solution:
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        
        x = A
        y = (x+1)//2
        while (y < x):
            x = y
            y = (x + A // x) // 2
        
        return x

solution = Solution()
A = 16
print(solution.sqrt(A))

A = 20
print(solution.sqrt(A))