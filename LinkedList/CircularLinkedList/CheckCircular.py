import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))
from SingleLinkedList.SingleLinkedList import SingleLinkedList
from CircularLinkedList import CircularLinkedList

"""
     Checking whether the linked list is circular or not
"""

def check_circular(linked_list):
    if linked_list. head:
        temp_node = linked_list.head
        while temp_node:
            temp_node = temp_node.next
            if temp_node == linked_list.head:
                print("Linked List was circular")
                return
        print("Linked list was Linear")
        return
    print("Linked List was Empty")


