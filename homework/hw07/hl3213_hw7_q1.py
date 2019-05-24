from LinkedBinaryTree import LinkedBinaryTree

class EmptyTree(Exception):
    pass

def min_and_max(bin_tree):
    if bin_tree.size == 0:
        raise EmptyTree
    '''
    min_max = [bin_tree.root.data, bin_tree.root.data]
    def subtree_min_and_max(subtree_root):
        if subtree_root.left is not None:
            subtree_min_and_max(subtree_root.left)
        if subtree_root.right is not None:
            subtree_min_and_max(subtree_root.right)

        if subtree_root.data < min_max[0]:
            min_max[0] = subtree_root.data
        if subtree_root.data > min_max[1]:
            min_max[1] = subtree_root.data

    subtree_min_and_max(bin_tree.root)
    return (min_max[0], min_max[1])
    '''
    def subtree_min_and_max(subtree_root):
        left_tree = (bin_tree.root.data, bin_tree.root.data)
        right_tree = (bin_tree.root.data, bin_tree.root.data)
        if subtree_root.left is not None:
            #print("going left:", subtree_root.data)
            left_tree = subtree_min_and_max(subtree_root.left)
        if subtree_root.right is not None:
            #print("going right:". subtree_root.data)
            right_tree = subtree_min_and_max(subtree_root.right)
        print("sub:", subtree_root.data)
        print("l:", left_tree)
        print("r:", right_tree)
        if subtree_root.data < left_tree[0]:
            left_tree = (subtree_root.data, left_tree[1])
        if subtree_root.data > left_tree[1]:
            left_tree = (left_tree[0], subtree_root.data)
        if subtree_root.data < right_tree[0]:
            right_tree = (subtree_root.data, right_tree[1])
        if subtree_root.data > right_tree[1]:
            right_tree = (right_tree[0], subtree_root.data)
        
        
    return subtree_min_and_max(bin_tree.root)

def main():
    n5 = LinkedBinaryTree.Node(5)
    n1 = LinkedBinaryTree.Node(1)
    n8 = LinkedBinaryTree.Node(8)
    n4 = LinkedBinaryTree.Node(4)
    n9 = LinkedBinaryTree.Node(9, n5, n1)
    n2 = LinkedBinaryTree.Node(2, n9)
    n7 = LinkedBinaryTree.Node(7, n8, n4)
    n3 = LinkedBinaryTree.Node(3, n2, n7)
    tree = LinkedBinaryTree(n3)
    min_and_max(tree)
main()
