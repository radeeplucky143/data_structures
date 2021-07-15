import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList.SingleLinkedList import SingleLinkedList
from CircularLinkedList.CircularLinkedList import CircularLinkedList
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

"""
     Finding the unique Element in Linked List
     Unique Element can be find out only if we pass odd number of elements and only one value should be unique 
     otherwise function doesn't return proper result.
"""


def find_unique_element(linked_list):
    if linked_list.head:
        unique_value = 0
        temp_node = linked_list.head
        while temp_node:
            unique_value = unique_value ^ temp_node.data
            temp_node = temp_node.next
            if temp_node == linked_list.head:
                break
        print("Unique Element in this Linked List : {}".format(unique_value))
        return
    print("Linked List is Empty")