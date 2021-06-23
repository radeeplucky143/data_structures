import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList


nodes = int(input("Enter the number of nodes: "))
linked_list = SingleLinkedList()
for _ in range(nodes):
    linked_list.insert_back(int(input("Enter the data value: ")))

data = int(input("Enter the data value: "))
linked_list.delete(data)
linked_list.print_list()



