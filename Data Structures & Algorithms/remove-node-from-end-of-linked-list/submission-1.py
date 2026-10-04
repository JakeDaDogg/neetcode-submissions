# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            sz += 1
        
        res = dummy = ListNode(0,head)
        i = 0
        while dummy and dummy.next:
            if i == sz - n:
                dummy.next = dummy.next.next
            dummy = dummy.next
            i += 1
        
        return res.next