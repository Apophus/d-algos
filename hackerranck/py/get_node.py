class SinglyLinkedListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

  
def getNode(llist, positionFromTail):
    curr = llist
    llist_length = 0
    while curr.next is not None:
        llist_length += 1
        curr = curr.next
    
    curr = llist
    index = llist_length - positionFromTail
    
    while index:
        curr = curr.next
        index -= 1
    
    return curr.data
    
    