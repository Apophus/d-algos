class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head,k):
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            kth = self.getKth(prev_group, k)
            if not kth:
                break

            next_group = kth.next

            prev, curr = next_group, prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        return  dummy.next

    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return  curr

