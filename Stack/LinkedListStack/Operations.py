import sys
from os.path import dirname, abspath

sys.path.append(dirname(abspath(__file__)))
from LinkedListStack import LinkedListStack

elements = int(input("Enter no of elements: "))
linked_list_stack = LinkedListStack()

linked_list_stack.isEmpty()

for _ in range(elements):
    data = int(input("Enter the data value: "))
    linked_list_stack.push(data)

linked_list_stack.print()
linked_list_stack.pop()
linked_list_stack.print()
linked_list_stack.peek()
linked_list_stack.isEmpty()
