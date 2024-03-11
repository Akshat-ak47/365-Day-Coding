'''
PRETTYPRINT
Print concentric rectangular pattern in a 2d matrix. 

Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.

Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = 2*A - 1
        
        matrix = [[0]*n for _ in range(n)]
        
        for i in range(A):
            for j in range (i, n-i):
                matrix[i][j] = A - i
                matrix[j][i] = A - i
                matrix[n-i-1][j] = A - i
                matrix[j][n-i-1] = A - i
                
        return matrix
    
A = 3
solution = Solution()
result = solution.prettyPrint(A)
for row in result:
    print(' '.join(map(str, row)))