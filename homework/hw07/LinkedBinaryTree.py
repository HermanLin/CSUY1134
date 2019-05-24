import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, root):
        if (root is None):
            return 0
        else:
            left_count = self.subtree_count(root.left)
            right_count = self.subtree_count(root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, root):
        if (root is None):
            return 0
        else:
            left_sum = self.subtree_sum(root.left)
            right_sum = self.subtree_sum(root.right)
            return root.data + left_sum + right_sum


    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, root):
        if (root.left is None and root.right is None):
            return 0
        elif (root.left is  None):
            return 1 + self.subtree_height(root.right)
        elif (root.right is  None):
            return 1 + self.subtree_height(root.left)
        else:
            left_height = self.subtree_height(root.left)
            right_height = self.subtree_height(root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, root):
        if(root is None):
            return
        else:
            yield root
            yield from self.subtree_preorder(root.left)
            yield from self.subtree_preorder(root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_postorder(root.left)
            yield from self.subtree_postorder(root.right)
            yield root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_inorder(root.left)
            yield root
            yield from self.subtree_inorder(root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data

    #===== hl3213_hw7_q2 =====#
    def leaves_list(self):
        if self.root is None:
            return []
        leaves = []
        def leaves_list_helper(subtree_root):
            if subtree_root.left is None and subtree_root.right is None:
                leaves.append(subtree_root.data)
            else:
                if subtree_root.left is not None:
                    leaves_list_helper(subtree_root.left)
                if subtree_root.right is not None:
                    leaves_list_helper(subtree_root.right)
        leaves_list_helper(self.root)
        return leaves
        
    #===== hl3213_hw7_q4 =====#
    def iterative_inorder(self):
        if self.root is None:
            return

        curr_node = self.root
        #stor_node = Node()
        while curr_node is not None:
            if curr_node.left is None:
                yield curr_node.data
                curr_node = curr_node.right
            else:
                stor_node = curr_node.left
                while stor_node.right is not None and stor_node.right is not curr_node:
                    stor_node = stor_node.right
                if stor_node.right is None:
                    stor_node.right = curr_node
                    curr_node = curr_node.left
                else:
                    stor_node.right = None
                    yield curr_node.data
                    curr_node = curr_node.right
