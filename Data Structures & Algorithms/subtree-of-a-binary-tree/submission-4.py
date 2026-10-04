class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return (dfs(root.left, subroot.left) and dfs(root.right, subroot.right))
            else:
                return False
        if not subRoot:
            return True
        if not root: return False

        if dfs(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))