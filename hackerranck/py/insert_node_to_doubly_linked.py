class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def sortedInsert(llist, data):
    # Write your code here
    curr = llist
    new_node = DoublyLinkedListNode(data)
    #case 1 list is empty
    if llist is None:
        llist = new_node
        
    #case 2 data < head
    elif data < llist.data:
        new_node.next = llist
        llist.prev = new_node
        llist = new_node
    
    #case 3 insert somewhere after head.
    else:
        #traverse to the specific position.
        while curr.next and curr.data < data:
            curr = curr.next
        
        #insert at the end        
        if curr.next == None and curr.data < data:
            curr.next = new_node
            new_node.prev = curr
         #insert at a position before the end    
        else:
            previous = curr.prev
            #update previous node
            previous.next = new_node
            new_node.prev = previous
             #update current node
            new_node.next = curr
            curr.prev = new_node
            
                
    return llist