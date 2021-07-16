class Node:
    """     Class used to create Node:
                    : data(param)  ==  used to store data
                    : next(param)  ==  Pointer pointing to next Node

                    : next(type)     ==  Node(class)
                    : data(type)     ==  int, str
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    """      Class used to create a SingleLinkedList Data Structure
                    : head(param)   ==  Pointing to First Node of SLL
                    : tail(param)     ==  Pointing to Last Node of SLL
                    : data_type(param)  ==  stores the datatype of data inside Node

                    : head(type)  == Node(class)
                    : tail(type)    ==  Node(class)
                    : data_type(type)  == int, str
    """
    def __init__(self):
        """     created SingleLinkedList and initializes the head, tail, data_type to None.
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
            print(f"\033[31mValueError for {__name__} class variable : data_type   Expected DataTypes : [int, str]\033[0m\n")


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
        if self.head is None:
            self.set_data_type(data)
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
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
        if self.head is None:
            self.set_data_type(data)
            self.head = new_node
            self.tail = self.head
            print(f"\033[32mInsertion at Head Successful\033[0m")
        else:
            self.tail.next = new_node
            self.tail = new_node
            print(f"\033[32mInsertion at Tail Successful\033[0m")


    def insert_pos(self, data, position):
        """  This function is used to Insert the Node at defined position If possible
               and make sure the inserted Node contains the data with same data type.
                                        : data(param)   ==  Inserted value
                                        : position(param) == position to insert

                                        : data(type)      ==   int,str,float
                                        : position(type)  == int
        """
        if not isinstance(position, int):
            print(f"\033[31mValueError for 'position' Arguement  Expected DataType: {int}\033[0m")
            return
        if not self.check_data_type(data):
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
                print(f"\033[32mInsertion at Head Successful\033[0m")
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
                            print(f"\033[32mInsertion at Tail Successful\033[0m")
                            return
                        x = self.get_suffix(position)
                        print(f"\033[32mInsertion at {position}{x} position Successful\033[0m")
                        return
                    count += 1
                    temp_node = temp_node.next
        print(f"\033[31mIndexOutOfBounds Insertion\033[0m")


    def search(self, data):
        """     This Function is used to search for the first Instance matched in the LinkedList.
                                        : data(param)   ==  Inserted value
                                        : data(type)      ==   int,str,float
        """
        if not self.check_data_type(data):
            return
        temp_node = self.head
        position = 1
        while temp_node:
            if temp_node.data == data:
                print("\033[33m{} Found at {}{} Position\033[0m".format(data, position, self.get_suffix(position)))
                return
            position += 1
            temp_node = temp_node.next
        print("\033[33m{} Not Found in LinkedList\033[0m".format(data))


    def search_all(self, data):
        """     This Function is used to search for all Instances matched in the LinkedList.
                                            : data(param)   ==  Inserted value
                                            : data(type)      ==   int,str,float
        """
        if not self.check_data_type(data):
            return
        temp_node = self.head
        position = 1
        found = False
        while temp_node:
            if temp_node.data == data:
                print("\033[33m{} Found at {}{} Position\033[0m".format(data, position, self.get_suffix(position)))
                found = True
            position += 1
            temp_node = temp_node.next
        if not found:
            print("\033[33m{} Not Found in LinkedList\033[0m".format(data))


    def search_pos(self, position):
        """    This Function is used to search for the Instance at particular position in LinkedList.
                                : position(param)   ==  position in LinkedList
                                : position(type)  ==   int
        """
        if not isinstance(position, int):
            print(f"\033[31mValueError for 'position' Arguement  Expected DataType: {int}\033[0m")
            return
        if position >= 1:
            temp_node = self.head
            count = 1
            while temp_node:
                if count == position:
                    print("\033[33mElement at {}{} position : {}\033[0m".format(position, self.get_suffix(position), temp_node.data))
                    return
                count += 1
                temp_node = temp_node.next
        print("\033[31mIndexOutOfBounds Search\033[0m")


    def delete_head(self):
        """   This Function is used to delete the head  Node If present.
        """
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
                self.data_type = None
            else:
                self.head = self.head.next
            print(f"\033[32mDeletion at Head Successful\033[0m")
            return
        print("\033[35mLinkedList was empty\033[0m")


    def delete_tail(self):
        """    This Function is used to delete the tail Node If Present.
        """
        if self.tail:
            if self.head == self.tail:
                print(f"\033[32mDeletion at Head Successful\033[0m")
                self.head = self.tail = None
                self.data_type = None
            else:
                temp_node = self.head
                while temp_node.next != self.tail:
                    temp_node = temp_node.next
                self.tail = temp_node
                self.tail.next = None
                print(f"\033[32mDeletion at Tail Successful\033[0m")
            return
        print("\033[35mLinkedList was empty\033[0m")


    def delete(self, data):
        """     This Function is used to delete First matched Instance .
                                : data(param)  == data to be deleted
                                : data (type)    == int, str
        """
        if not self.check_data_type(data):
            return
        if self.head:
            if self.head.data == data:
                if self.head == self.tail:
                    self.head = self.tail = None
                    self.data_type = None
                else:
                    self.head = self.head.next
                print(f"\033[32mDeletion at Head Successful\033[0m")
                return
            else:
                prev_node = self.head
                temp_node = self.head.next
                position = 2
                while temp_node:
                    if temp_node.data == data:
                        if temp_node.next:
                            next_node = temp_node.next
                            prev_node.next = next_node
                            del temp_node
                            print("\033[32mDeletion at {}{} position Successful\033[0m".format(position, self.get_suffix(position)))
                        else:
                            self.delete_tail()
                            print(f"\033[32mDeletion at Tail Successful\033[0m")
                        return
                    position += 1
                    prev_node = temp_node
                    temp_node = temp_node.next
            print(f"\033[33m{data} Not Found in LinkedList\033[0m")
            return
        print("\033[35mLinked List was Empty\033[0m")


    def delete_all(self, data):
        """     This Function is used to delete all the Instances matched.
                                : data(param)  == data to be deleted
                                : data (type)    == int, str
        """
        if not self.check_data_type(data):
            return
        if self.head:
            operation = False
            if self.head.data == data:
                self.delete_head()
                operation = True
                print(f"\033[32mDeletion at Head Successful\033[0m")
            prev_node = self.head
            temp_node = self.head.next
            position = 2
            while temp_node:
                if temp_node.data == data:
                    operation = True
                    if temp_node.next:
                        next_node = temp_node.next
                        prev_node.next = next_node
                        print("\033[32mDeletion at {}{} position Successful\033[0m".format(position, self.get_suffix(position)))
                    else:
                        self.delete_tail()
                        print(f"\033[32mDeletion at Tail Successful\033[0m")
                        return
                    temp_node = next_node
                else:
                    prev_node = temp_node
                    temp_node = temp_node.next
                position += 1
            if not operation:
                print(f"\033[33m{data} Not Found in LinkedList\033[0m")
            return
        print("\033[35mLinked List was Empty\033[0m")


    def delete_pos(self, position):
        """     This Function is used to delete the element at position If present.
                            : position(param)  == position of element to be deleted
                            : position(type) == int
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
                                print(f"\033[32mDeletion at Tail Successful\033[0m")
                                return
                            print("\033[32mDeletion at {}{} position successful\033[0m".format(position, self.get_suffix(position)))
                            return
                        break
                    temp_node = temp_node.next
                    count += 1
            print("\033[31mIndexOutOfBounds\033[0m")
            return
        print("\033[31mIndexOutOfBounds\033[0m")


    def print_list(self):
        """     Print the Nodes in SingleLinkedList
                    i.e, view is similar to LinkedList.
        """
        temp_node = self.head
        while temp_node:
            print("\033[34m{}->".format(temp_node.data), end="")
            temp_node = temp_node.next
        print("\033[34mNULL\033[0m")


    def get_head(self):
        """     Returns the data present in the Head Node.
                    returns None If data was not present.
        """
        if self.head:
            return self.head.data
        return None


    def get_tail(self):
        """     Returns the data present in the Tail Node.
                    returns None If data was not present.
        """
        if self.tail:
            return self.tail.data
        return None