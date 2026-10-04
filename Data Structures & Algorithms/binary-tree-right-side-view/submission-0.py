# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        res = []
        level = 0
        while len(queue) > 0:
            loq = len(queue)
            for i in range(loq):
                temp = queue.popleft()
                
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                if i == loq-1:
                    res.append(temp.val)
            level += 1
        return res

        