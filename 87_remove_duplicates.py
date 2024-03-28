'''
Remove Duplicates from Sorted Array II

Problem Description

Remove Duplicates from the Sorted Array
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
Note that even though we want you to return the new length, make sure to change the original array as well in place

Example Input
A = [1,1,1,2]


Example Output
3
'''
class Solution:
    def removeDuplicates(self, A):        
        if len(A) <= 2:
            return len(A)

        count = 2
        for i in range(2, len(A)):
            if A[i] != A[count - 2]:
                A[count] = A[i]
                count += 1

        return count

solution = Solution()
A = [1,1,1,2]
print(solution.removeDuplicates(A))