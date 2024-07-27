# Lucky Numbers in a Matrix

# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        row_min = float('-inf')
        for i in range(row):
            r_min = min(matrix[i])
            row_min = max(row_min, r_min)
        
        col_max = float('inf')
        for j in range(col):
            c_max = max(matrix[i][j] for i in range(row))
            col_max = min(c_max, col_max)
        
        if row_min == col_max:
            return [row_min]
        else:
            return []