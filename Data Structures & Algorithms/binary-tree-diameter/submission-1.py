# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, res = self.dfs(root)
        return res
        
    def dfs(self, root):
        
        if not root:
            return 0, 0
        else:
            lb, lmd = self.dfs(root.left)
            rb, rmd = self.dfs(root.right)
            max_diameter = max(lmd, rmd, lb+rb)
            max_depth = max(1+lb, 1+rb)

            #print(max_depth, max_diameter)

            return max_depth, max_diameter