'''
Identical Binary Trees

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Return  0 / 1  ( 0 for false, 1 for true ) for this problem

Example :

Input : 

   1       1
  / \     / \
 2   3   2   3

Output : 
  1 
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if not A and not B:
            return 1
        if not A or not B:
            return 0
        
        return (A.val == B.val) and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)

A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)

B = TreeNode(1)
B.left = TreeNode(2)
B.right = TreeNode(3)

solution = Solution()

result = solution.isSameTree(A, B)
print(result)