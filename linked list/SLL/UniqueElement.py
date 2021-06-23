import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList


def find_unique_element(linked_list):
        unique_value = 0
        temp_node = linked_list.head
        while temp_node:
            unique_value = unique_value ^ temp_node.data
            temp_node = temp_node.next
        return unique_value

nodes = int(input("Enter the number of nodes: "))
linked_list = SingleLinkedList()
for _ in range(nodes):
    linked_list.insert_back(int(input("Enter the data : ")))

print("Unique element: {}".format(find_unique_element(linked_list)))


