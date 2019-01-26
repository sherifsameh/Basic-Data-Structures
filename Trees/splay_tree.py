from bst import TreeNode, BST



class SplayTree(BST):
    ############################## SPLAYING ##############################
    def zig_zig(self, start_node, left_children=True):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # start zig-zig
        if left_children:
            print("Left zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_left(parent.right)
            parent.set_right(grand_parent)
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig-zig")
            child.parent = grand_parent.parent
            grand_parent.set_right(parent.left)
            parent.set_left(grand_parent)
            parent.set_right(child.left)
            child.set_left(parent)
        #child is now the grand-parent
        return child

    def zig_zag(self, start_node, left_right_children=True):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # start zig-zag
        if left_right_children:
            print("Left-Right zig-zag")
            child.parent = grand_parent.parent
            grand_parent.set_left(child.right)
            parent.set_right(child.left)
            child.set_right(grand_parent)
            child.set_left(parent)
            pass
        else:
            print("Right-Left zig-zag")
            child.parent = grand_parent.parent
            grand_parent.set_right(child.left)
            parent.set_left(child.right)
            child.set_left(grand_parent)
            child.set_right(parent)
        return child

    def zig(self, start_node, left_child=True):
        child = start_node
        parent = child.parent
        if left_child:
            print("Left zig")
            child.parent = parent.parent
            parent.set_left(child.right)
            child.set_right(parent)
        else:
            print("Right zig")
            child.parent = parent.parent
            parent.set_right(child.left)
            child.set_left(parent)
        return child

    def __splaying(self, start_node):
        child = start_node
        parent = child.parent
        grand_parent = parent.parent
        # get the operation type
        if grand_parent is None:
            if child.is_left_child():
                root = self.zig(child, left_child=True)
            else:
                root = self.zig(child, left_child=False)
        else:
            # left -> left
            if parent.is_left_child() and child.is_left_child():
                grand_parent = self.zig_zig(child, left_children=True)
            # left -> right
            elif parent.is_left_child() and not child.is_left_child():
                grand_parent = self.zig_zag(child, left_right_children=True)
            # right -> left
            elif not parent.is_left_child() and child.is_left_child():
                grand_parent = self.zig_zag(child, left_right_children=False)
            # right -> right
            else:
                grand_parent = self.zig_zig(child, left_children=False)
            if grand_parent.parent is not None:
                root = self.__splaying(grand_parent)
            else:
                root = grand_parent
        return root
    

    def splay(self, start_node):
        self.root = self.__splaying(start_node)


    ############################## INSERTION ##############################
    def __insert(self, value, start_node):
        if value == start_node.data:
            return
        elif value < start_node.data:
            if start_node.left:
                self.__insert(value, start_node.left)
            else:
                start_node.set_left( TreeNode(value) )
                # splay
                self.splay(start_node.left)
        else:
            if start_node.right:
                self.__insert(value, start_node.right)
            else:
                start_node.set_right( TreeNode(value) )
                # splay
                self.splay(start_node.right)

    def insert(self, value):
        assert type(value) in {int, float}, "You can insert only numbers!"
        self.__insert(value, self.root)

    # don't forget to disable:
    # traverse
    # height
    # balance
    # perfect
    # ...






if __name__ == "__main__":
    # example from Data Structures and Algorithm in Python (page: 514)
    stree = SplayTree(8)
    stree.root.set_left(TreeNode(3))
    stree.root.left.set_right(TreeNode(4))
    stree.root.left.right.set_right(TreeNode(6))
    stree.root.left.right.right.set_left(TreeNode(5))
    stree.root.left.right.right.set_right(TreeNode(7))
    stree.root.set_right(TreeNode(10))
    stree.root.right.set_right(TreeNode(11))
    stree.root.right.right.set_right(TreeNode(12))
    stree.root.right.right.right.set_right(TreeNode(16))
    stree.root.right.right.right.right.set_left(TreeNode(13))
    stree.root.right.right.right.right.set_right(TreeNode(17))
    stree.insert(14)
    print(stree)

    # # test Left zig-zig
    # stree = SplayTree(30)
    # stree.insert(20)
    # stree.insert(10)
    # print(stree)
    # stree.splay(stree.root.left.left)
    # print(stree)
    # print('='*50)

    # # test Right zig-zig
    # stree = SplayTree(10)
    # stree.insert(20)
    # stree.insert(30)
    # print(stree)
    # stree.splay(stree.root.right.right)
    # print(stree)
    # print('='*50)

    # # test Right-left zig-zig
    # stree = SplayTree(10)
    # stree.insert(30)
    # stree.insert(20)
    # print(stree)
    # stree.splay(stree.root.right.left)
    # print(stree)
    # print('='*50)

    # # test Left-right zig-zig
    # stree = SplayTree(30)
    # stree.insert(10)
    # stree.insert(20)
    # print(stree)
    # stree.splay(stree.root.left.right)
    # print(stree)
    # print('='*50)

    # # test right zig
    # stree = SplayTree(10)
    # stree.insert(20)
    # print(stree)
    # stree.splay(stree.root.right)
    # print(stree)
    # print('='*50)

    # # test left zig
    # stree = SplayTree(20)
    # stree.insert(10)
    # print(stree)
    # stree.splay(stree.root.left)
    # print(stree)
    # print('='*50)