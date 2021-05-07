# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 : return l2
        elif not l2 : return l1
        else:
            l3 = ListNode()
            l4 = l3
            while( l1 or l2 ):
                if not l1:
                    l4.next = l2
                    break
                elif not l2:
                    l4.next = l1
                    break
                elif l1.val <= l2.val :
                    l4.next = l1
                    l4 = l4.next
                    l1 = l1.next
                    continue
                elif l2.val < l1.val:
                    l4.next = l2
                    l4 = l4.next
                    l2 = l2.next
                    continue
        l3 = l3.next
        return l3
