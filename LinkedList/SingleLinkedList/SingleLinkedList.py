class Node:
    """     Class used to create Node:
                    : data(param)  ==  used to store data
                    : next(param)  ==  Pointer pointing to next Node

                    : next(type)     ==  Node(class)
                    : data(type)     ==  int,float,str
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    """      Class used to create a SingleLinkedList Data Structure
                    : head(param)   ==  Pointing to First Element of SLL
                    : tail(param)     ==  Pointing to Last Element of SLL
                    : data_type(param)  ==  stores the type of data inside Node

                    : head(type)  == Node(class)
                    : tail(type)    ==  Node(class)
                    : data_type(type)  == int,float,str
    """
    def __init__(self):
        """
              created SingleLinkedList and initializes the head and tail to None.
        """
        self.head = None
        self.tail = None
        self.data_type = None


    def set_data_type(self, data):
        """
              This Function is used to set the data_type attribute
              which helps in maintaining the same data type along the LinkedList.
                        : data(param)   ==  Inserted value
                        : data(type)      ==   int,str,float
        """
        if isinstance(data, int):
            self.data_type = int
        elif isinstance(data, float):
            self.data_type = float
        elif isinstance(data, str):
            self.data_type = str
        else:
            print("DataTypes should be [int,float,str]")


    def insert_front(self, data):
        """
               This function is used to Insert the Node at front and make sure the inserted Node
               contains the data with same data type.
                            : data(param)   ==  Inserted value
                            : data(type)      ==   int,str,float
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        new_node = Node(data)
        if self.head is None:
            self.set_data_type(data)
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node


    def insert_back(self, data):
        """
              This function is used to Insert the Node at back and make sure the inserted Node
               contains the data with same data type.
                                : data(param)   ==  Inserted value
                                : data(type)      ==   int,str,float
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        new_node = Node(data)
        if self.head is None:
            self.set_data_type(data)
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node


    def insert_pos(self, data, position):
        """
              This function is used to Insert the Node at defined position If possible
               and make sure the inserted Node contains the data with same data type.
                                        : data(param)   ==  Inserted value
                                        : position(param) == position to insert

                                        : data(type)      ==   int,str,float
                                        : position(type)  == int
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        if position >= 1:
            if position == 1:
                new_node = Node(data)
                if self.head is None:
                    self.set_data_type(data)
                    self.head = new_node
                    self.tail = self.head
                else:
                    new_node.next = self.head
                    self.head = new_node
                return
            else:
                temp_node = self.head
                count = 1
                new_node = Node(data)
                while temp_node:
                    if count == position - 1:
                        next_node = temp_node.next
                        temp_node.next = new_node
                        new_node.next = next_node
                        if next_node is None:
                            self.tail = new_node
                        return
                    count += 1
                    temp_node = temp_node.next
        print("Position out of bounds")


    def search(self, data):
        """
              This Function is used to search for the first Instance matched in the LinkedList.
                                        : data(param)   ==  Inserted value
                                        : data(type)      ==   int,str,float
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        temp_node = self.head
        position = 1
        while temp_node:
            if temp_node.data == data:
                print("{} Found at Position {}".format(data, position))
                return
            position += 1
            temp_node = temp_node.next
        print("{} Not Found".format(data))


    def search_all(self, data):
        """
              This Function is used to search for all Instances matched in the LinkedList.
                                            : data(param)   ==  Inserted value
                                            : data(type)      ==   int,str,float
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        temp_node = self.head
        position = 1
        found = False
        while temp_node:
            if temp_node.data == data:
                print("{} Found at Position {}".format(data, position))
                found = True
            position += 1
            temp_node = temp_node.next
        if not found:
            print("{} Not Found".format(data))


    def search_pos(self, position):
        """
                This Function is used to search for the first Instance matched in the LinkedList.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        if position >= 1:
            temp_node = self.head
            count = 1
            while temp_node:
                if count == position:
                    print("Element at {} position : {}".format(position, temp_node.data))
                    return
                count += 1
                temp_node = temp_node.next
        print("Position out of Bounds")


    def delete_head(self):
        """
            This Function is used to delete the head positioned Node If present.
        """
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return
        print("LinkedList was empty")


    def delete_tail(self):
        """
            This Function is used to delete the tail Node If Present.
        """
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
        """
                This Function is used to delete First matched Instance .
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
        if self.head:
            if self.head.data == data:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
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
        """
            This Function is used to delete all the Instances matched.
        """
        if self.data_type is not None:
            if isinstance(data, self.data_type):
                print("Data should be of type : {}".format(self.data_type))
                return
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


    def delete_pos(self, position):
        """
                This Function is used to delete the element at position If present.
        """
        if position >= 1:
            if position == 1:
                self.delete_head()
                return
            else:
                count = 1
                temp_node = self.head
                while temp_node:
                    if count == position - 1:
                        if temp_node.next:
                            next_node = temp_node.next.next
                            temp_node.next = next_node
                            if next_node is None:
                                self.tail = temp_node
                            return
                        break
                    temp_node = temp_node.next
                    count += 1
            print("position out of Bounds")
            return
        print("Position out of Bounds")


    def print_list(self):
        """
            Print the Entire LinkedList.
        """
        temp_node = self.head
        while temp_node:
            print(temp_node.data, end='->')
            temp_node = temp_node.next
        print("NULL")


    def get_head(self):
        """
            Returns the data present in the Head Node.
        """
        return self.head.data


    def get_tail(self):
        """
            Returns the data present in the Tail Node.
        """
        return self.tail.data
