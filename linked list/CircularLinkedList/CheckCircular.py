import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))
from CircularLinkedList.CircularLinkedList import CircularLinkedList
from SingleLinkedList.SingleLinkedList import SingleLinkedList

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


nodes = int(input("Enter the number of nodes: "))
circular_linked_list = CircularLinkedList()
single_linked_list = SingleLinkedList()
for _ in range(nodes):
    data = int(input("Enter the data : "))
    circular_linked_list.insert_front(data)
    single_linked_list.insert_front(data)


check_circular(circular_linked_list)
check_circular(single_linked_list)
