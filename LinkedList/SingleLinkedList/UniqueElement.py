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


nodes = int(input("Enter number of nodes: "))
single_linked_list = SingleLinkedList()
for _ in range(nodes):
    single_linked_list.insert_back(int(input("Enter the data : ")))

find_unique_element(single_linked_list)