#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(llist, data, position):
    # Write your code here

    start = llist
    if position == 0:
        return SinglyLinkedListNode(data, llist)
    while position > 1:
        llist = llist.next
        position -= 1
        print(position, data)
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist.next
    llist.next = new_node
    return start


if __name__ == '__main__':
    node1 = SinglyLinkedListNode(16)
    node2 = SinglyLinkedListNode(13)
    node1.next = node2
    node2.next = SinglyLinkedListNode(7)
