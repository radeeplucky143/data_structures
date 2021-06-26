import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList.SingleLinkedList import SingleLinkedList
from CircularLinkedList.CircularLinkedList import CircularLinkedList
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

"""
      This program is used to reverse the linked list of any type 
"""


def reverse_list(linked_list):
    if isinstance(linked_list, SingleLinkedList):
        reversed_list = SingleLinkedList()
        temp_node = linked_list.head
        while temp_node:
            reversed_list.insert_back(temp_node.data)
            temp_node = temp_node.next
        return reversed_list
    elif isinstance(linked_list, CircularLinkedList):
        reversed_list = CircularLinkedList()
        temp_node = linked_list.head
        while temp_node:
            reversed_list.insert_back(temp_node.data)
            temp_node = temp_node.next
            if temp_node.next == linked_list.head:
                break
        return reversed_list
    elif isinstance(linked_list, DoublyLinkedList):
        reversed_list = DoublyLinkedList()
        temp_node = linked_list.head
        while temp_node:
            reversed_list.insert_back(temp_node.data)
            temp_node = temp_node.next
        return reversed_list
    else:
        print("Incorrect Arguement Passed")