# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        L = ListNode()
        if not head: return None
        else: 
            L.next = head
            p1 = L
            p2 = head
        if not head.next : return head
        else: p3 = head.next
        while(True):
            p2.next = p3.next
            p3.next = p2
            p1.next = p3
            if not p2.next:break
            elif not p2.next.next:break
            else:
                p1 = p2
                p3 = p2.next.next
                p2 = p2.next
        return L.next 

