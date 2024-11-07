class Solution:
    def reverseList(self, head):
        previous, current = None, head
        while current is not None:
            _next = current.next #temp variable
            current.next = previous #set next to None disconnect node
            previous = current # push head behind
            current = _next
            
        return previous