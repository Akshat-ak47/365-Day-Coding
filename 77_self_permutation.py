'''
Self Permutation

Problem Description
You are given two strings A and B.
Check whether there exists any permutation of both A and B such that they are equal.

Return a single integer 1 if its exists, 0 otherwise.

Example Input
Input 1:
A = 'scaler'
B = 'relasc'

Input 2:
A = 'scaler'
B = 'interviewbit'

Example Output
Output 1:
1
Output 2:
0
'''
from collections import Counter
class Solution:
    def permuteStrings(self, A, B):
        map_A = Counter(A)
        map_B = Counter(B)
        
        if map_A == map_B:
            return 1
        else:
            return 0

solution = Solution()
A = "scaler"
B = "relacs"
print(solution.permuteStrings(A, B))

A = "SCALER"
B = "relacs"
print(solution.permuteStrings(A, B))