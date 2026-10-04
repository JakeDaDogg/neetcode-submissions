# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        loc_Max = -float('inf')
        res = []
        def dfs(node, locMax):
            nonlocal res
            curMax = locMax
            if node.val >= locMax:
                res.append(node)
                curMax = node.val
            if node.left:
                dfs(node.left, curMax)
            if node.right:
                dfs(node.right, curMax)
        dfs(root, loc_Max)
        return len(res)