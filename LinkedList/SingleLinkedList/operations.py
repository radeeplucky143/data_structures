import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from SingleLinkedList import SingleLinkedList

list1 = SingleLinkedList()
list1.insert_pos(23, 1)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))
list1.insert_pos(89, 2)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))
list1.insert_pos(29, 2)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))
list1.insert_pos(12, 4)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))
list1.insert_pos(56, 3)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))
list1.print_list()

