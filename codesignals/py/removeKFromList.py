# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l


def solution1(l, k):
    if l == None:
        return None
    if l.next == None and l.value == k:
        return None
    if l.next == None and l.value != k:
        return l
    else:
        while l.value == k:
            l = l.next
            if l == None:
                return None
        current = l
        ahead = current.next
        while ahead is not None:
            if ahead.value == k:
                current.next = ahead.next
                ahead = current.next
            else:
                current = ahead
                ahead = ahead.next
        return l


def solution2(l, k):
    m = l
    while m:
        if m.next and m.next.value == k:
            m.next = m.next.next
        else:
            m = m.next
    if l and l.value == k:
        return l.next
    return l
