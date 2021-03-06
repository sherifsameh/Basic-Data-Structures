class Item:
    """Basic object for item inside Priority Queue"""
    def __init__(self, data, priority):
        self.data = data
        # priority has to be an integer bigger than or equal to zero
        assert type(priority) == int and priority >= 0, \
                                "priority can't be negative values"
        self.priority = priority

    def __repr__(self):
        return "({}, {})".format(self.data, self.priority)



class PriorityQueue:
    """Basic object for the Priority Queue data structure where highest priority
    is zero."""
    def __init__(self):
        self.container = []

    def __repr__(self):
        top_border = '─┬'
        middle = ' │'
        down_border = '─┴'
        for item in self.container:
            width = len(str(item))+2 #2: for a space before & after item
            top_border += ('─'*width) + '┬'
            middle += " {} │".format(item)
            down_border += ('─'*width) + '┴'
        # add extension
        top_border += '─'
        middle += ' '
        down_border += '─'
        return "{}\n{}\n{}".format(top_border, middle, down_border)

    def __len__(self):
        return len(self.container)

    def enqueue(self, item):
        """Insert value into the Priority Queue"""
        if len(self) == 0:
            self.container.append(item)
        else:
            new_data, new_priority = item.data, item.priority
            for i, _item in enumerate(self.container):
                curr_data, curr_priority = _item.data, _item.priority
                if new_priority <= curr_priority:
                    self.container = self.container[:i] + [item]\
                                         + self.container[i:]
                    break

    def remove_min(self):
        """Removes value from the Priority Queue (Queue's head)"""
        return self.container.pop(0)

    def get_max_priority(self):
        """Returns the highest-priority item to be enqueued"""
        return self.container[0]

    def get_min_priority(self):
        """Returns the lowest-priority item to be enqueued"""
        return self.container[-1]

    def is_empty(self):
        """Checks if the Priority Queue is empty"""
        return self.container == 0

    def clear(self):
        """Clears the whole Priority Queue"""
        self.container = []




if __name__ == "__main__":
    q = PriorityQueue()
    q.enqueue(Item(1, 10))
    q.enqueue(Item(100, 0))
    q.enqueue(Item(100, 0))
    q.enqueue(Item("hello", 1))
    q.enqueue(Item([1,2], 8))
    q.enqueue(Item(-1, 6))
    print(q)
    q.dequeue()
    print(q)
    q.clear()
    print(q)