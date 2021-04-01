# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # print(l1.val)
        # print(l1.next.val)
        # print(l1.next.next.val)
        def print_ln(l) :
            while True :
                print(l.val)
                l = l.next
                if not l : break

        # print(l2.val)
        # print(l2.next.val)
        # print(l2.next.next.val)

        # print_ln(l1)
        # print_ln(l2)

        ans = l3 = ListNode()
        tag = 0
        while l1 or l2 or tag > 0 : # 只要进入了新的一次循环，我们一定要保证当前这个新的l3是一个最终一定要在答案里的数字
            # 当前循环处理第i位
            if not l1 : l1 = ListNode() #如果第1个数字的第i位不存在则补上前导0
            if not l2 : l2 = ListNode() # 同上
            l3.val = l1.val + l2.val + tag # 答案的第i位=两数第i位之和+第i-1位的进位
            if l3.val >= 10 : # 答案第i位需进位时
                tag = 1 # 第i位的进位赋值为1
                l3.val -= 10 # 答案第i位取个位数
            else : tag = 0  #答案第i位无需进位，那么第i位进位赋值为0
            # 此时第i位的事情处理完毕，准备为处理第i+1位做准备
            l1 = l1.next #第一个数的指针指向i+1位，可能不存在
            l2 = l2.next #第二个数的指针指向i+1位，可能不存在
            if not l1 and not l2 and tag == 0 : #答案的第i+1位一定不存在
                break
            #如果程序能运行到此处，答案的第i+1位一定存在，继续循环
            l3.next = ListNode() # 新建下个节点
            l3 = l3.next # l3的指针指向答案的第i+1个节点
        return ans


        while l1 or l2 or tag > 0 : # 只要进入了新的一次循环，我们一定要保证当前这个新的l3是一个最终一定要在答案里的数字
            # 当前循环处理第i位
            if not l1 and l2: # 答案的第i位 对应第i位l1没了l2还有
                l3.val = l2.val + tag # 算第i位的l3
                l2 = l2.next    #l2指向第i+1位
            elif not l2 and l1: # 答案的第i位 对应第i位l2没了l1还有
                l3.val=l1.val+tag # 算第i位的l3
                l1 = l1.next    #l1指向第i+1位
            elif not l2 and not l1 and tag>0: # 答案的第i位 对应第i位l1没了l2没了，但还有进位
                l3.val = tag # 算第i位的l3
            else: # 答案的第i位 对应第i位l1和l2还有
                l3.val = l1.val + l2.val + tag # 算第i位的l3
                l1 = l1.next    #l1指向第i+1位
                l2 = l2.next    #l2指向第i+1位
            if l3.val >= 10 : # 答案第i位需进位时
                tag = 1 # 第i位的进位赋值为1
                l3.val -= 10 # 答案第i位取个位数
            else : tag = 0  #答案第i位无需进位，那么第i位进位赋值为0
            if not l1 and not l2 and tag == 0 : #答案的第i+1位一定不存在
                break
            #如果程序能运行到此处，答案的第i+1位一定存在，继续循环
            l3.next = ListNode() # 新建下个节点
            l3 = l3.next # l3的指针指向答案的第i+1个节点
        return ans