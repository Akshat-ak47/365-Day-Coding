
'''
Problem - Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
 Example :

 Given the below binary tree and sum = 22,

'''
# Explain
#                5
#               / \
#              4   8
#             /   / \
#            11  13  4
#           /  \      \
#          7    2      1
#  return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#  Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def hasPathSum(A, B):
    if not A:
        return 0
    
    def dfs(node, current_sum):
        if not node.left and not node.right:
            return 1 if current_sum + node.val == B else 0
        
        left_result = dfs(node.left, current_sum+node.val) if node.left else 0
        right_result = dfs(node.right, current_sum+node.val) if node.right else 0
        
        return left_result or right_result
    
    return dfs(A, 0)
        
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

target_sum = 22
print(hasPathSum(root, target_sum))  # Output: 1 (True)
