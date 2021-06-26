import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList

"""
     Finding the unique Element in Single Linked List 
"""


def find_unique_element(linked_list):
    unique_value = 0
    temp_node = linked_list.head
    while temp_node:
        unique_value = unique_value ^ temp_node.data
        temp_node = temp_node.next
    print("Unique Element in this Linked List : {}".format(unique_value))