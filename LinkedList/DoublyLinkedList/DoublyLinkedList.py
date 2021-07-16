class Node:
    """     Class used to create Node:
                        : data(param)  ==  used to store data
                        : next(param)  ==  Pointer pointing to next Node
                        : prev(param) == Pointer pointing to prev Node

                        : next(type)     ==  Node(class)
                        : prev(type)     ==  Node(class)
                        : data(type)     ==  int, str
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """      Class used to create a DoublyLinkedList Data Structure
                        : head(param)   ==  Pointing to First Node of DLL
                        : tail(param)     ==  Pointing to Last Node of DLL
                        : data_type(param)  ==  stores the datatype of data inside Node

                        : head(type)  == Node(class)
                        : tail(type)    ==  Node(class)
                        : data_type(type)  == int, str
    """
    def __init__(self):
        """     created DoublyLinkedList and initializes the head, tail, data_type to None.
        """
        self.head = None
        self.tail = None
        self.data_type = None
        print("\033[32mSingleLinkedList created successfully\033[0m")

    @staticmethod
    def get_suffix(position):
        """ This method is used to provide suffix for the Integers like 1st,2nd,3rd,4th etc...
        """
        if position == 1:
            return 'st'
        elif position == 2:
            return 'nd'
        elif position == 3:
            return 'rd'
        else:
            return 'th'

    def set_data_type(self, data):
        """  This Function is used to set the value to data_type attribute
              which helps in maintaining the same data type across the LinkedList.
                        : data(param)   ==  Inserted value
                        : data(type)      ==   int,str
        """
        if isinstance(data, int):
            self.data_type = int
        elif isinstance(data, str):
            self.data_type = str
        else:
            print(
                f"\033[31mValueError for {__name__} class variable : data_type   Expected DataTypes : [int, str]\033[0m\n")


    def check_data_type(self, data):
        """     This function is used to check whether the inserted data is
                    same as LinkedList data type or not.
        """
        if self.data_type is not None:
            if not isinstance(data, self.data_type):
                print("\033[31mValueError for Arguement : 'data'  Expected DataType: {}\033[0m".format(self.data_type))
                return False
        return True


    def insert_front(self, data):
        """   This function is used to Insert the Node at front and make sure the inserted Node
                       contains the data with same data type.
                                    : data(param)   ==  Inserted value
                                    : data(type)      ==   int,str
        """
        if not self.check_data_type(data):
            return
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.set_data_type(data)
            self.head = self.tail = new_node
        print(f"\033[32mInsertion at Head Successful\033[0m")


    def insert_back(self, data):
        """   This function is used to Insert the Node at back and make sure the inserted Node
                       contains the data with same data type.
                                        : data(param)   ==  Inserted value
                                        : data(type)      ==   int,str,float
        """
        if not self.check_data_type(data):
            return
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            print(f"\033[32mInsertion at Tail Successful\033[0m")
        else:
            self.set_data_type(data)
            self.head = self.tail = new_node
            print(f"\033[32mInsertion at Head Successful\033[0m")


    def insert_pos(self, data, pos):
        if pos >= 1:
            if pos == 1:
                self.insert_front(data)
                return
            else:
                count = 1
                temp_node = self.head
                new_node = Node(data)
                while temp_node:
                    if count == pos - 1:
                        next_node = temp_node.next
                        temp_node.next = new_node
                        new_node.prev = temp_node
                        new_node.next = next_node
                        if next_node is None:
                            self.tail = new_node
                        else:
                            next_node.prev = new_node
                        return
                    count += 1
                    temp_node = temp_node.next
        print("Index out of Bounds")

    def search(self, data):
        temp_node = self.head
        position = 1
        while temp_node:
            if temp_node.data == data:
                print("{} number  found at position {}".format(data, position))
                return
            position += 1
            temp_node = temp_node.next
        print("Element not found")


    def search_all(self, data):
        temp_node = self.head
        position = 1
        found = False
        while temp_node:
            if temp_node.data == data:
                print("{} number  found at position {}".format(data, position))
                found = True
            position += 1
            temp_node = temp_node.next
        if not found:
            print("Element not found")


    def search_pos(self, pos):
        if pos >= 1:
            temp_node = self.head
            count = 1
            while temp_node:
                if count == pos:
                    print("Element at {} position : {}".format(pos, temp_node.data))
                    return
                count += 1
                temp_node = temp_node.next
        print("Index out of Bounds")


    def delete_head(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        print("LinkedList was empty")

    def delete_tail(self):
        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                temp_node = self.head
                while temp_node.next != self.tail:
                    temp_node = temp_node.next
                self.tail = temp_node
                self.tail.next = None
            return
        print("LinkedList was empty")



    def delete(self, data):
        if self.head:
            if self.head.data == data:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                print("Deleted at Head Position")
                return
            else:
                prev_node = self.head
                temp_node = self.head.next
                while temp_node:
                    if temp_node.data == data:
                        if temp_node.next:
                            next_node = temp_node.next
                            prev_node.next = next_node
                            next_node.prev = prev_node
                            del temp_node
                            print("Deleted Successfully")
                        else:
                            self.delete_tail()
                            print("Deleted at Tail position")
                        return
                    prev_node = temp_node
                    temp_node = temp_node.next
            print("Element not Found")
            return
        print("Linked List was Empty")


    def delete_all(self, data):
        if self.head:
            operation = False
            if self.head.data == data:
                self.delete_head()
                operation = True
                print("Deleted at Head Position")
            prev_node = self.head
            temp_node = self.head.next
            while temp_node:
                if temp_node.data == data:
                    operation = True
                    if temp_node.next:
                        next_node = temp_node.next
                        prev_node.next = next_node
                        next_node.prev = prev_node
                        print("Deleted Successfully")
                    else:
                        self.delete_tail()
                        print("Deleted at Tail position")
                        return
                    temp_node = next_node
                else:
                    prev_node = temp_node
                    temp_node = temp_node.next
            if not operation:
                print("Element not Found")
            return
        print("Linked List was Empty")


    def delete_pos(self, pos):
        if pos >= 1:
            if pos == 1:
                self.delete_head()
                return
            else:
                count = 1
                temp_node = self.head
                while temp_node:
                    if count == pos - 1:
                        if temp_node.next:
                            next_node = temp_node.next.next
                            temp_node.next = next_node
                            if next_node is None:
                                self.tail = temp_node
                            else:
                                next_node.prev = temp_node
                            return
                        break
                    temp_node = temp_node.next
                    count += 1
            print("Index out of Bounds")
            return
        print("Index out of Bounds")


    def print_list(self):
        if self.head:
            temp_node = self.head
            print("NULL", end='<->')
            while temp_node:
                print(temp_node.data, end='<->')
                temp_node = temp_node.next
            print("NULL")
            return
        print("NULL")


    def print_reverse(self):
        if self.tail:
            temp_node = self.tail
            print("NULL", end="<->")
            while temp_node:
                print(temp_node.data, end='<->')
                temp_node = temp_node.prev
            print("NULL")
            return
        print("NULL")


    def get_head(self):
        if self.head:
            return self.head.data
        return None

    def get_tail(self):
        if self.tail:
            return self.tail.data
        return None
