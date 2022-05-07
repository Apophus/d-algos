def insertNodeAtTail(head, data):
    cur = head
    if head == None:
        return SinglyLinkedListNode(data)
    while cur.next != None:
        cur = cur.next
    cur.next = SinglyLinkedListNode(data)
    return head