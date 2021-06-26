import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from DoublyLinkedList import DoublyLinkedList

list1 = DoublyLinkedList()

list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(72, 1)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(65, 2)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(924, 3)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(65 ,2)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_front(65)
list1.insert_back(65)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))



list1.search_pos(0)
list1.search_pos(1)
list1.search_pos(4)
list1.search_pos(6)
list1.search_pos(9)


