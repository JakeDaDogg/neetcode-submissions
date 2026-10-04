"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dih = {None : None}
        cur = head

        while cur:
            copy = Node(cur.val)
            dih[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = dih[cur]
            copy.next = dih[cur.next]
            copy.random = dih[cur.random]
            cur = cur.next
        
        return dih[head]
            

        
        
