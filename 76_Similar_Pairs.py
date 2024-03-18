'''
Similar Pairs

Problem Description

Given an integer array A of size N, you need to find the count of pairs  (i, j) such that:

i < j
j - i <= B
A[i] == A[j]
Return the count of such pairs modulo 109 + 7.
'''

class Solution:
    def solve(self, A, B):
        count = 0
        window = {}
        
        for i, num in enumerate(A):
            if num in window:
                count += window[num]
            window[num] = window.get(num, 0) + 1
            if i - B >= 0:
                window[A[i - B]] -= 1
                if window[A[i - B]] == 0:
                    del window[A[i - B]]
        
        return count % (10**9 + 7)

solution = Solution()
A = [1, 2, 1, 3, 1, 4]
B = 2
print(solution.solve(A , B))