'''
Remove Element from Array
Problem Description

Given an array A and a value B, remove all the instances of that value in the array.
Also, return the number of elements left in the array after the operation. It does not matter what is left beyond the expected length.
Try to do it in less than linear additional space complexity.

Input Format
The first argument is an integer array A.
The second argument is an integer B.


Output Format
Return an integer denoting the number of elements left in the array after the operation, 
also update the given array A.
'''

class Solution:
    def removeElement(self, A, B):
        n = len(A)
        i = 0
        
        for j in range(n):
            if A[j] != B:
                A[i] = A[j]
                i += 1
        
        return i


solution = Solution()
A = [4, 1, 1, 2, 1, 3]
B = 1
length = solution.removeElement(A, B)
print("Length:", length)
print("Array A:", A[:length])
