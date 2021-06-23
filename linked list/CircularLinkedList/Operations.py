import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from CircularLinkedList import CircularLinkedList


nodes = int(input("Enter the number of nodes: "))
linked_list = CircularLinkedList()
for _ in range(nodes):
    linked_list.insert_front(int(input("Enter the data value: ")))

linked_list.print_list()
linked_list.get_head()
linked_list.get_tail()
