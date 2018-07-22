class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #不做拆分，统一处理，做了很多重复判断，时间复杂度较大
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = ListNode(0)
        idx = cur
        rmd = 0
        while l1 or l2:
            if l1:
                rmd += l1.val
                l1 = l1.next
            if l2:
                rmd += l2.val
                l2 = l2.next
            node = ListNode(rmd%10)
            rmd = rmd//10
            idx.next = node
            idx = idx.next
        if rmd > 0:
            node = ListNode(rmd%10)
            idx.next = node
        return cur.next

    #拆分处理，代码上看冗余较多，但相比第一种在性能上有提升
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = ListNode(0)
        idx = cur
        rmd = 0
        while l1 and l2:
            rmd += l1.val +l2.val
            node = ListNode(rmd%10)
            rmd = rmd//10
            idx.next = node
            idx = idx.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            rmd += l1.val
            node = ListNode(rmd%10)
            rmd = rmd//10
            idx.next = node
            idx = idx.next
            l1 = l1.next
        while l2:
            rmd += l2.val
            node = ListNode(rmd%10)
            rmd = rmd//10
            idx.next = node
            idx = idx.next
            l2 = l2.next
        if rmd > 0:
            node = ListNode(rmd%10)
            idx.next = node
        return cur.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    ret = Solution.addTwoNumbers(Solution(), l1, l2)
    while ret:
        print('{}'.format(ret.val))
        ret = ret.next
