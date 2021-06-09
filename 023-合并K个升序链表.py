
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        size = len(lists)
        if size == 0:
            return None
        cishu = size // 2
        a = lists
        while(size > 1):
            b = []
            for i in range(cishu):
                b.append(Solution.Twomerge(a[2 * i],a[2 * i + 1]))
            if size % 2 == 1:
                b.append(a[-1])
            a = b
            size = len(a)
            cishu = size // 2
        return a[0]
        def Twomerge(l1,l2):
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
