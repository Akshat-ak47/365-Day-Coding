'''
Level Order
Problem Description
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderTraversal(A):
    if not A:
        return []

    result = []
    current_level = [A]

    while current_level:
        next_level = []
        current_values = []

        for node in current_level:
            current_values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(current_values)
        current_level = next_level

    return result



root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(levelOrderTraversal(root1))

root2 = TreeNode(1)
root2.left = TreeNode(6)
root2.right = TreeNode(2)
root2.right.left = TreeNode(3)
print(levelOrderTraversal(root2))
