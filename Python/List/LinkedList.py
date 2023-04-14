from Python.Node.Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def size(self):
        return self.length

    def clear(self):
        self.length = 0
        self.head = None

    def add(self, value):
        try:
            new_node = Node(value)
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node

            self.length += 1
            return True
        except:
            print('Exception: Not able to add data')
            return False

    def addAt(self, index, value):
        try:
            new_node = Node(value)
            if index >= self.length:
                print('Index out of range')
                return False
            if index == 0:
                new_node.next = self.head
                self.head = new_node
                self.length += 1
                return True
            else:
                current = self.head
                previous = self.head
                i = 0
                while current:
                    if i == index:
                        previous.next = new_node
                        new_node.next = current
                        self.length += 1
                        return True
                    previous = current
                    current = current.next
                    i += 1
                print('not a valid index')
                return False
        except:
            print('Exception: Not able to add data')
            return False
    
    def remove(self, value):
        try:
            if self.length > 0:
                if self.head.item == value:
                    self.head = self.head.next
                    self.length -= 1
                    return True
                else:
                    previous = self.head
                    current = self.head
                    while current:
                        if current.item == value:
                            previous.next = current.next
                            self.length -= 1
                            return True
                        previous = current
                        current = current.next

                print('Item not found')
            else:
                print('List is empty')
            
            return False
        except:
            print('Exception: Not able to remove data')
            return False

    def removeAt(self, index):
        try:
            if index < 0:
                print('Invalid index')
                return False
            if index >= self.length:
                print('Index out of range')
                return False
            if self.length > 0:
                if index == 0:
                    self.head = self.head.next
                    self.length -= 1
                    return True
                else:
                    i = 0
                    previous = self.head
                    current = self.head
                    while current:
                        if i == index:
                            previous.next = current.next
                            self.length -= 1
                            return True
                        previous = current
                        current = current.next
                        i += 1
            else:
                print('List is empty')
            
            return False
        except:
            print('Exception: Not able to remove data')
            return False

    def get(self, index):
        try:
            if index < 0:
                print('Invalid index')
                return None
            if self.length == 0:
                print('List is empty')
                return None
            elif self.length <= index:
                print('Index is out of range')
                return None
            else:
                i = 0
                current = self.head
                while current:
                    if i == index:
                        return current.item
                    i += 1
                    current = current.next
            print('Item not found')
            return None
        except:
            print('Exception: Not able to find data')
            return None

    def indexOf(self, value):
        try:
            if self.length == 0:
                print('List is empty')
                return -1
            else:
                current = self.head
                i = 0
                while current:
                    if current.item == value:
                        return i
                    i += 1
                    current = current.next
                print('Item not found')
                return -1
        except:
            print('Exception: Not able to find data')
            return -1

    def tolist(self):
        list = []
        current = self.head
        while current:
            list.append(current.item)
            current = current.next
        
        return list