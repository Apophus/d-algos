def reversePrint(llist):
    # Write your code here
    head = llist
    res = []
    while head is not None:
        res.append(head.data)
        head = head.next

    for i in res[::-1]:
        print(i)