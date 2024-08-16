def removeDuplicates(llist):
    # Write your code here
    curr = llist
    if not curr: return
    
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return llist
