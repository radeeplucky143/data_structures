import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList

def reverse_list(single_linked_list):
    reverse_linked_list = SingleLinkedList()
    temp_node = single_linked_list.head
    while temp_node:
        reverse_linked_list.insert_front(temp_node.data)
        temp_node = temp_node.next
    return reverse_linked_list


nodes = int(input("Enter the number of nodes: "))
linked_list = SingleLinkedList()
for _ in range(nodes):
    linked_list.insert_back(int(input("Enter the data value: ")))

reversed_list = reverse_list(linked_list)
reversed_list.print_list()
