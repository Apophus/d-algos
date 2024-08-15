
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        list_copy = {None: None} #old_node : new_node
        curr = head
        
        while curr:
            new_node = Node(curr.val)
            list_copy[curr] = new_node
            curr = curr.next
        
        curr = head  
        while curr:
            new_node = list_copy[curr]
            new_node.next = list_copy[curr.next]
            new_node.random = list_copy[curr.random]
            curr = curr.next 
            
        return list_copy[head]