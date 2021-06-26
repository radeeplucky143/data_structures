import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList

"""
      This program is used to reverse the single linked list
"""


def reverse_list(single_linked_list):
    reverse_linked_list = SingleLinkedList()
    temp_node = single_linked_list.head
    while temp_node:
        reverse_linked_list.insert_front(temp_node.data)
        temp_node = temp_node.next
    return reverse_linked_list