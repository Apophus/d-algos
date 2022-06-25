class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index == 0:
            return self.head.val
        else:
            current = self.head
            count = 0
            while current != None:
                if index == count:
                    return current.val
                count += 1
                current = current.next
            return -1

    def addAtHead(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        print(self.head.val, self.size)

    def addAtTail(self, val):
        newNode = ListNode(val)
        current = self.head
        while current.next != None:
            current = current.next
            print(current.val)
        current.next = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            count = 0
            current = self.head
            prev = None
            newNode = ListNode(val)
            while count != index and current.next != None:
                count += 1
                prev = current
                current = current.next
            if count == index:
                prev.next = newNode
                newNode.next = current
                self.size += 1

    def deleteAtIndex(self, index):
        if index == 0:
            ans = self.head.val
            newHead = self.head.next
            self.head = newHead
            self.size -= 1
            return ans
        else:
            count = 0
            current = self.head
            prev = None
            while count != index and current.next != None:
                prev = current
                current = current.next
                count += 1
            if count == index:
                prev.next = current.next
                self.size -= 1


if __name__ == '__main__':
    ll = MyLinkedList()
    ll.addAtHead(1)
    ll.addAtTail(3)
    ll.addAtIndex(1, 2)
