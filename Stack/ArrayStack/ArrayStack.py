class ArrayStack:

    def __init__(self):
        self.items = list()


    def push(self,data):
        self.items.append(data)


    def pop(self):
        if self.items:
            del self.items[-1]
        else:
            print("Stack was Empty")


    def peek(self):
        if self.items:
            print("Top Element: {}".format(self.items[-1]))
        else:
            print("Stack was Empty")


    def isEmpty(self):
        if self.items:
            print("not Empty")
            return
        print("Empty")


    def print_stack(self):
        for ele in self.items:
            print(ele, end=' ')
        print(end='\n')
