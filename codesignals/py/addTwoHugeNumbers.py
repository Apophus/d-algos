#Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(a, b):
    if not a and not b:
        return
    carry = 0
    temp_node = ListNode()
    while a or b:
        if a and b:
            sum_node = a.value + b.value + carry
            if sum_node > 9:
                carry += 1
            a.value = sum_node



