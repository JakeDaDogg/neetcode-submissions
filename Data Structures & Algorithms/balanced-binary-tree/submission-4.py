# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res, height = self.dfs(root)
        return res
    def dfs(self, root):
        if not root:
            return (True, 0)
        left, left_height = self.dfs(root.left)
        right, right_height = self.dfs(root.right)
        height_balance = True if abs(left_height - right_height) <= 1 else False
        node_balance = left and right
        return (height_balance and node_balance, max(left_height, right_height) + 1 ) 