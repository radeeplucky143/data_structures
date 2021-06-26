import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(dirname(abspath(__file__)))))
from LinkedList.SingleLinkedList.SingleLinkedList import SingleLinkedList

class LinkedListStack:

    def __init__(self):
        self.items = SingleLinkedList()


    def push(self, data):
        self.items.insert_back(data)


    def pop(self):
        self.items.delete_tail()


    def peek(self):
        data = self.items.get_tail()
        if data:
            print("Top Element : {}".format(data))
            return
        print("Stack is Empty")


    def isEmpty(self):
        if self.items.head:
            print("Stack is not Empty")
            return
        print("Stack is Empty")


    def print(self):
        temp_node = self.items.head
        while temp_node:
            print(temp_node.data, end=' ')
            temp_node = temp_node.next
        print(end='\n')