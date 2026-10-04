
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        maxlvl = -1
        def dfs(root, curlvl):
            if not root:
                return
            nonlocal maxlvl
            if curlvl > maxlvl:
                res.append(root.val)
                maxlvl = curlvl
            dfs(root.right, curlvl + 1)
            dfs(root.left, curlvl + 1)
        
        dfs(root, 0)
        return res