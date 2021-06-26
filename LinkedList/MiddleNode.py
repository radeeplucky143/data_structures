import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList.SingleLinkedList import SingleLinkedList
from CircularLinkedList.CircularLinkedList import CircularLinkedList
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

"""
      For the even number of nodes in a linked list we can select any one of the two middle nodes
      depending upon the condition use any one of the two functions.
"""

def get_second_middle_node(linked_list):
    if linked_list.head:
        first_ptr = linked_list.head
        second_ptr = linked_list.head
        while second_ptr.next and second_ptr.next != linked_list.head:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next
            if second_ptr.next and second_ptr.next != linked_list.head:
                second_ptr = second_ptr.next
        print(first_ptr.data)
        return
    print("Linked List is Empty")


def get_first_middle_node(linked_list):
    if linked_list.head:
        first_ptr = linked_list.head
        second_ptr = linked_list.head
        while second_ptr.next and second_ptr.next != linked_list.head:
            second_ptr = second_ptr.next
            if second_ptr.next and second_ptr.next != linked_list.head:
                first_ptr = first_ptr.next
                second_ptr = second_ptr.next
        print(first_ptr.data)
        return
    print("Linked List was Empty")