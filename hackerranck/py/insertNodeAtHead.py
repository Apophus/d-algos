def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    
    if llist:
        node.next = llist