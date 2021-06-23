import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from DoublyLinkedList import DoublyLinkedList


nodes = int(input("Enter no of nodes: "))
doubly_linked_list = DoublyLinkedList()
for _ in range(nodes):
    doubly_linked_list.insert_front(int(input("Enter the data : ")))

doubly_linked_list.print_list()
doubly_linked_list.print_list_reverse()
doubly_linked_list.get_head()
doubly_linked_list.get_tail()
