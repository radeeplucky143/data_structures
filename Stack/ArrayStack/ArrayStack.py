class ArrayStack:

    def __init__(self):
        self.items = list()


    def push(self, data):
        self.items.append(data)


    def pop(self):
        if self.items:
            del self.items[-1]
            return
        print("Stack is Empty")


    def peek(self):
        if self.items:
            print("Top Element: {}".format(self.items[-1]))
            return
        print("Stack is Empty")


    def isEmpty(self):
        if self.items:
            print("Stack is not Empty")
            return
        print("Stack is Empty")


    def print_stack(self):
        if self.items:
            for ele in self.items:
                print(ele, end=' ')
            print(end='\n')
            return
        print("Stack is Empty")
