class Node():
    """Basic object for the Node used for linked lists"""
    def __init__(self, item=None):
        self.data = item
        self.next = None

    def __repr__(self):
        """Represents Node object as a string"""
        data = self.data
        nxt = self.next.data if self.next else None
        return "Node: (item: {}, next: {})".format(data, nxt)
    


class LinkedList():
    """Basic object for the linked list"""
    def __init__(self, item=None):
        self.head = Node(item)
        self.length = 1 if item else 0


    def __repr__(self):
        """Represents the linked list as a string."""
        # NOTE: complexity of + operator is O(1) in lists and O(n) in string
        top_border = ['┌']
        middle = ['│']
        down_border = ['└']
        pointer = self.head
        while(pointer != None):
            item = pointer.data
            if item:
                width = len(str(item))+2 #2: for a space before & after an item
                top_border += (['─']*width) + ['┬']
                middle += [" {} →".format(item)]
                down_border += (['─']*width) + ['┴']
            pointer = pointer.next
        top_border += ['─']
        middle += [' ']
        down_border += ['─']
        return "{}\n{}\n{}".format(\
            "".join(top_border), "".join(middle), "".join(down_border))


    def __len__(self):
        """Gets the length of the linked list with complexity of O(1)"""
        return self.length


    def __fix_index(self, idx):
        """
        private method to make a sanity-check over the given index and fix it
        if it was -ve. It should return the index if it's valid. If the index is
        negative, then it converts it to positive index if possible.
        If the index has any error of any kind, it raises an appropriate error.
        """
        if type(idx) != int:
            msg = "idx must be an integer!"
            raise TypeError(msg)
        # handle negative index
        if idx <=-1 and abs(idx) <= self.length:
            idx += self.length
        # handle positive/negative indices
        elif abs(idx) >= self.length:
            msg = "max index for this linked list is " + str(self.length-1)
            raise IndexError(msg)
        else:
            pass #direct
        return idx
            

    def __getitem__(self, idx):
        """Retrieves the element at the given index. It allows -ve indexing"""
        # sanity check over given index
        idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            return self.head
        # iterate over the linked list
        counter = 0
        pointer = self.head
        while(pointer.next != None):
            counter += 1
            pointer = pointer.next
            if counter == idx:
                return pointer


    def __setitem__(self, idx):
        pass


    def is_empty(self):
        """Checks if linked list is empty"""
        return self.length == 0


    def add_front(self, item):
        """Adds node at the head of the linked list with complexity of O(1)"""
        if self.length == 0:
            self.head = Node(item)
        else:
            new_node = Node(self.head.data)
            new_node.next = self.head.next
            self.head = Node(item)
            self.head.next = new_node
        self.length += 1


    def add_end(self, item):
        """Adds node at the tail of the linked list with complexity of O(n)"""
        if self.length == 0:
            self.head = Node(item)
        else:
            pointer = self.head
            while(pointer.next != None):
                pointer = pointer.next
            # now pointer is the last node
            pointer.next = Node(item)
        self.length += 1


    def remove_front(self):
        """Removes the linked list head with complexity of O(1)"""
        if self.length > 0:
            self.head = self.head.next
            self.length -= 1


    def remove_end(self):
        """Removes the linked list tail with complexity of O(n)"""
        if self.length > 0:
            pointer = self.head
            while(pointer.next.next != None):
                pointer = pointer.next
            # now the pointer is the second last node
            pointer.next = None
            self.length -= 1


    def insert(self, idx, item):
        """Inserts a certain item at a given index into the linked list"""
        if idx <= -1 and abs(idx) <= self.length+1:
            idx += self.length+1
        else:
            idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            self.add_front(item)
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            new_node = Node(item)
            new_node.next = pointer.next
            pointer.next = new_node
            self.length += 1


    def remove(self, idx):
        """Removes a node at index=idx from the linked list"""
        idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            self.remove_front()
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            pointer.next = pointer.next.next
            self.length -= 1


    def insert_multiple(self, idx, lst):
        """Inserts multiple items into the linked list at once"""
        if idx <= -1 and abs(idx) <= self.length+1:
            idx += self.length+1
        else:
            idx = self.__fix_index(idx)
        # handle edge case
        if idx == 0:
            # NOTE: iterate over given list in reverse-order as add_front() is
            # faster than add_end()
            for i in range(len(lst)-1, -1, -1):
                self.add_front(lst[i])
        # handle general case
        else:
            counter = 0
            pointer = self.head
            while(counter != idx-1):  
                pointer = pointer.next
                counter += 1
            # pointer is now at (idx-1)
            # iterate over given list in reverse-order
            for item in lst:
                new_node = Node(item)
                new_node.next = pointer.next
                pointer.next = new_node
                # update pointer
                pointer = pointer.next
                self.length += 1


    def clear(self):
        """Removes all nodes within the linked list with complexity of O(1)"""
        self.head = Node()
        self.length = 0


    def reverse(self):
        """Reverses the whole linked list with complexity of O(n)"""
        rev = LinkedList()
        pointer = self.head
        while(pointer.next != None):
            rev.add_front(pointer.data)
            pointer = pointer.next
        rev.add_front(pointer.data)
        return rev




if __name__ == "__main__":
    l = LinkedList()
    print(l)
    l.add_front(6)   #6
    l.add_end(20)    #6 20
    print(l)
    l.insert(1, 10)  #6 10 20
    l.insert(-2, 999)#6 10 999 20
    l.insert_multiple(2, [1, 2, 3, 4])  #6 10 1 2 3 4 999 20
    l.insert(-9, -555)#-555 6 10 1 2 3 4 999 20
    print(l)
    print("LENGTH:", len(l))

    l.remove(-9)     #6 10 1 2 3 4 999 20
    l.remove(-2)     #6 10 1 2 3 4 20
    l.remove_front() #10 1 2 3 4 20
    l.remove_end()   #10 1 2 3 4
    l.remove(0)      #1 2 3 4
    print(l)
    print("LENGTH:", len(l))
    
    print(l[0], l[3], "\n")

    rev = l.reverse()#4 3 2 1
    print(rev)
    print("REV LENGTH:", len(rev))
    print(rev[1], rev[2])

    l.clear()
    print("Linked List is empty?", l.is_empty())
    print("Reversed Linked List is empty?", rev.is_empty())

