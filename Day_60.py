'''
Leaders in an array
Problem Description

Given an integer array A containing N distinct integers, you have to find all the leaders in the array A.

 An element is leader if it is strictly greater than all the elements to its right side.

NOTE:The rightmost element is always a leader.

Example Input
Input 1:

 A = [16, 17, 4, 3, 5, 2]
Input 2:

 A = [1, 2]


Example Output
Output 1:

 [17, 2, 5]
Output 2:

 [2]
 '''
 
def solve(A):
    n = len(A)
    right = A[n-1]
    
    if n==0:
        return []
        
    result = []
    for i in range(n-2, -1, -1):
        if A[i] > right:
            result.append(A[i])
            right = A[i]

    result.append(A[n-1])
    return result

A = [16, 17, 4, 3, 5, 2]
print(solve(A))
