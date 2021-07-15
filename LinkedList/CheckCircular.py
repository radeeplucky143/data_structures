import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList.SingleLinkedList import SingleLinkedList
from CircularLinkedList.CircularLinkedList import CircularLinkedList
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

"""
     check_circular function is used to check whether the linked_list was circular or not 
     It returns three values based upon the scenarios:
            LinkedList was Empty
            LinkedList was Linear
            LinkedList was Circular
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