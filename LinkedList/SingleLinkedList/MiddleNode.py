import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList

"""
      For the even number of nodes in a linked list we can select any one of the two middle nodes
      depending upon the condition use any one of the two functions.
"""

def get_second_middle_node(linked_list):
    first_ptr = linked_list.head
    second_ptr = linked_list.head
    while second_ptr.next:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next
        if second_ptr.next:
            second_ptr = second_ptr.next
    print(first_ptr.data)

def get_first_middle_node(linked_list):
    first_ptr = linked_list.head
    second_ptr = linked_list.head
    while second_ptr.next:
        second_ptr = second_ptr.next
        if second_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
    print(first_ptr.data)


nodes = int(input("Enter number of nodes: "))
single_linked_list = SingleLinkedList()
for _ in range(nodes):
    single_linked_list.insert_back(int(input("Enter the data : ")))

get_first_middle_node(single_linked_list)
get_second_middle_node(single_linked_list)
