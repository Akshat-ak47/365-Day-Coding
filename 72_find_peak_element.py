'''
Find a peak element

Given an array of integers A, find and return the peak element in it.
An array element is peak if it is NOT smaller than its neighbors. 
For corner elements, we need to consider only one neighbor. 
For example, for input array {5, 10, 20, 15}, 20 is the only peak element.

Following corner cases give better idea about the problem.
1) If input array is sorted in strictly increasing order, the last element is always a peak element. 
For example, 5 is peak element in {1, 2, 3, 4, 5}.
2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 
10 is the peak element in {10, 9, 8, 7, 6}.
Note: It is guranteed that the answer is unique.
'''
class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)
        return A[n-1]

solution = Solution()
A = [4, 7, 1, 9, 2]
print(solution.solve(A))