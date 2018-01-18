class Queue():
    """Basic object for the Queue data structure"""
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
        """Insert value into the Queue"""
        self.container.append(item)

    def dequeue(self):
        """Removes value from the Queue (Queue's head)"""
        return self.container.pop(0)

    def get_head(self):
        """Returns the Qeueu head (first element to be enqueued) """
        return self.container[0]

    def get_tail(self):
        """Returns the Qeueu tail (last element to be enqueued) """
        return self.container[-1]

    def is_empty(self):
        """Checks if the Queue is empty"""
        return len(self) == 0

    def clear(self):
        """Clears the whole Queue"""
        self.container = []



if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    print(q)
    q.enqueue(1)
    q.enqueue(8)
    q.enqueue(9)
    print(q.get_head())
    print(q)
    q.dequeue()
    print(q)
    q.clear()
    print(q)