class Solution:
    def reverseList(self, head):
        res = []
        previous, current = None, head
        while current is not None:
            _next = current.next
            current.next = previous
            previous = current
            current = _next
            
        return previous
            