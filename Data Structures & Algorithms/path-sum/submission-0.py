# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            return self.dfs(root, 0, targetSum)
            

    def dfs(self, root, pathSum, targetSum):
        if not root:
            return False

        pathSum = root.val + pathSum
        if not root.left and not root.right:
            return pathSum == targetSum

        return self.dfs(root.left, pathSum, targetSum) or self.dfs(root.right, pathSum, targetSum)
