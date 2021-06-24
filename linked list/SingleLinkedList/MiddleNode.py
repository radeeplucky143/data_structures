import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList

def get_second_middle_node(linked_list):
        first_ptr = linked_list.head
        second_ptr = linked_list.head
        while second_ptr.next != None:
            first_ptr = first_ptr.next
            second_ptr= second_ptr.next
            if second_ptr.next != None:
                second_ptr = second_ptr.next
        print(first_ptr.data)

def get_first_middle_node(linked_list):
        first_ptr = linked_list.head
        second_ptr = linked_list.head
        while second_ptr.next != None:
            second_ptr= second_ptr.next
            if second_ptr.next != None:
                first_ptr = first_ptr.next
                second_ptr = second_ptr.next
        print(first_ptr.data)



