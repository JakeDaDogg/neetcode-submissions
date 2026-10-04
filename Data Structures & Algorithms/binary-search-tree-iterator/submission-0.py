# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.stack = []
        self.curr = root
        while self.stack or self.curr:
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                self.curr = self.stack.pop() 
                self.inorder.append(self.curr.val)
                self.curr = self.curr.right        

    def next(self) -> int:
        ele = self.inorder.pop(0)
        return ele

    def hasNext(self) -> bool:
        if self.inorder:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()