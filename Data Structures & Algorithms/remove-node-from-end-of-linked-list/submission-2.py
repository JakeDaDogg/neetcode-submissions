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
            sz += 1
            dummy = dummy.next
        
        if sz == n:
            return head.next
        
        curr = head
        cnt = 1
        while curr and curr.next:
            if cnt == sz - n:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
                cnt += 1
        return head