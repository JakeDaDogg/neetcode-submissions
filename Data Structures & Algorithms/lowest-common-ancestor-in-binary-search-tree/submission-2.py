class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # every left node is smaller than every right node in the subtree
        def dfs(node, p, q):
            if not node:
                return None
            if (p.val < node.val and q.val > node.val) or (q.val < node.val and p.val > node.val):
                return node
            if p.val == node.val or q.val == node.val:
                return node
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            if p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
        
        return dfs(root, p, q)