# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):

        if p.val < root.val and q.val < root.val:
            return self.dfs(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.dfs(root.right, p, q)

        else: return root
        
        