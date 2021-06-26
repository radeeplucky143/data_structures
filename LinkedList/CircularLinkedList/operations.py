import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from CircularLinkedList import CircularLinkedList

list1 = CircularLinkedList()
list1.delete_head()
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.delete_tail()
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))


list1.insert_back(90)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.delete_head()
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))


list1.insert_back(80)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.delete_tail()
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.insert_back(40)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.insert_back(30)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.insert_back(20)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.insert_back(10)
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.delete_tail()
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))

list1.delete_head()
list1.print_list()
print("Head : {}".format(list1.get_head()))
print("Tail: {}\n".format(list1.get_tail()))
