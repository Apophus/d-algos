# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def sortList(self, head):
        if not head or not head.next:
             return head
         
        left = head
        right = self.get_mid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def get_mid(self, head):
        """Get the midpoint of the linkedlist

        Args:
            head (ListNode or None): head of the linkedlist

        Returns:
            ListNode: the slow pointer
        """
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
        
    def merge(self, list1, list2):
        temp = ListNode()
        tail = temp
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return temp.next