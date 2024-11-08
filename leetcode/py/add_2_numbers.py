# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        dummy = ListNode
        curr = dummy
        while l1 or l2 or carry_over:
            val1  = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            _sum = val1 + val2 + carry_over
            carry_over = _sum // 10
            val = _sum%10

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next



