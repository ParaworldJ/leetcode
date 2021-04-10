# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ##################两个指针：
        first = head
        second = ListNode()
        second.next = head
        if not head:
            return head
        t = n - 1
        while(t):
            first = first.next
            if not first:
                return head
            t = t - 1
        flag = 0
        while(first.next):
            second = second.next
            first = first.next
            flag = flag + 1
        if flag == 0:
            head = head.next
        else:
            second.next = second.next.next
        return head