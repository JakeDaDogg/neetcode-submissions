# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        gn = 0
        def dfs(node, stk):
            nonlocal gn
            if not node: return
            is_good = node.val >= max(stk) if stk else True
            stk.append(node.val)
            if is_good: gn += 1
            dfs(node.left, stk)
            dfs(node.right, stk)

            stk.pop()
            return 
        dfs(root, [])
        return gn