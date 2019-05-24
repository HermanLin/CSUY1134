from LinkedBinaryTree import LinkedBinaryTree

def is_height_balanced(bin_tree):
    def is_height_balanced_helper(subtree_root):        
        if subtree_root is None:
            return 0
        
        left_height = is_height_balanced_helper(subtree_root.left)
        if left_height == -1:
            return -1
        right_height = is_height_balanced_helper(subtree_root.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return is_height_balanced_helper(bin_tree.root) >= 0
