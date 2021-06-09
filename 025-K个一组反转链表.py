# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:return None
        p1 = head
        j = 0
        while(p1):
            a = []
            for i in range(0,k):
                print(p1.val)
                if not p1:break
                else:
                    a.append(p1)
                    p1 = p1.next
            print(a[0].val,a[1].val)
            if len(a) < k:
                if j == 0:
                    return head
                else:
                    for i in range(len(a)):
                        p2.next = a[i]
                        p2 = p2.next
            else:
                if j == 0:
                    result = ListNode()
                    result.next = a[-1]
                    p2 = result
                for i in range(0,k):
                    p2.next = a.pop()
                    p2 = p2.next
                    p2.next = None
            j = j + 1
        return result
a1 = ListNode()
a2 = ListNode()
a1.val = 1
a1.next = a2
a2.val = 2
a = Solution()
p = a.reverseKGroup(a1,2)
while(p):
    print(p.val)
    p = p.next