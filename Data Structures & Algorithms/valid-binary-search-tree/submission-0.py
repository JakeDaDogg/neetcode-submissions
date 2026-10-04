class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        def dfs(node, low=-float('inf'), high=float('inf')):
            if node == None:
                return True

            if not (low < node.val < high):
                return False

            left_valid = dfs(node.left, low, node.val)
            right_valid = dfs(node.right, node.val, high)
            
            return left_valid and right_valid
        return dfs(root)