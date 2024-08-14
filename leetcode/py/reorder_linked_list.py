# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #reverse second half of the list
        second_half = slow.next 
        previous = slow.next = None
        while second_half:
            temp = second_half.next
            second_half.next = previous
            previous = second_half
            second_half = temp
        
        #merge the halves
        first, second = head, previous
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            