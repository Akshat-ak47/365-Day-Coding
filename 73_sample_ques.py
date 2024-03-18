'''
Sample Question

Given two integers A and B. Find the sum of these integers as a modulo of 107.
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        total = A + B
        return total % 10**7

solution = Solution()
print(solution.solve(2,3))