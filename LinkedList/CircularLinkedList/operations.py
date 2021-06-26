import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from CircularLinkedList import CircularLinkedList
from CheckCircular import check_circular

list1 = CircularLinkedList()

list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(34, 1)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(94, 1)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(924, 3)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

list1.insert_pos(67, 3)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail : {}\n".format(list1.get_tail()))

check_circular(list1)
