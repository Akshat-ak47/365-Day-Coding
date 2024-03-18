'''
Remove Consecutive Characters

Problem Description
 
 

Given a string A and integer B, remove all consecutive same characters that have length exactly B.


NOTE : All the consecutive same characters that have length exactly B will be removed simultaneously.

Example Input
Input 1:

A = "aabcd"
B = 2
Input 2:

A = "aabbccd"
B = 2


Example Output
Output 1:

 "bcd"
Output 2:

 "d"
'''

class Solution:
    def solve(self, A, B):
        if B == 1:
            return ""

        N = len(A)
        res = ""
        i = 0
        
        while i < N:
            cnt = 1
            j = i + 1
            while j < N and A[j] == A[i]:
                j += 1
                cnt += 1
            if cnt != B:
                while i < j:
                    res += A[i]
                    i += 1
            i = j
        return res

# Example usage:
solver = Solution()
A = "aabcd"
B = 2
print(solver.solve(A, B))  # Output: "bcd"
