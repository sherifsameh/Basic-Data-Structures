from binary_tree import TreeNode, BinaryTree


class MinHeap(BinaryTree):
    def __init__(self, value):
        if type(value) == list:
            lst = sorted(value)
            self.root = self.heapify(lst)
        else:
            self.root = TreeNode(value)

    def heapify(self, lst):
        length = len(lst)
        assert length >0, "Given List must have values!!"
        if length == 1:
            node = TreeNode(lst[0])
        elif length == 2:
            node = TreeNode(lst[0])
            node.left = TreeNode(lst[1])
        else:
            node = TreeNode(lst[0])
            node.left = self.heapify(lst[1::2])
            node.right = self.heapify(lst[2::2])
        return node




if __name__ == "__main__":
    h = MinHeap([4,3,1,2, 5, 80, 10, 20, 30, 40, 52, 10])
    print(h)