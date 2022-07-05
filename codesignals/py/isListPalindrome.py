# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    res = []
    if not l:
        return True
    while l is not None:
        res.append(l.value)
        l = l.next

    if res == res[::-1]:
        return True
    else:
        return False
