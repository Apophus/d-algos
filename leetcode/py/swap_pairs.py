# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr and curr.next:
            #save pointers
            next_pair = curr.next.next
            _next_node = curr.next

            #reverse pair
            _next_node.next = curr
            curr.next = next_pair
            prev.next = _next_node

            #update pointers
            prev = curr
            curr = next_pair

        return dummy.next
