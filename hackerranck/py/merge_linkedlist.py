# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    
    

def mergeLists(head1, head2):
    
    temp = SinglyLinkedListNode(0)
    tail = temp

    while head1 and head2:
        if head1.data > head2.data:
            tail.next = head2
            head2 = head2.next
        else:
            tail.next = head1 
            head1 = head1.next 
    
        tail = tail.next 
        
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2
    
    return temp.next
