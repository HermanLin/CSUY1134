from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    if bst.is_empty():
        return None
    else:
        result = find_min_abs_diff_helper(bst.root, bst.root.item.key, bst.root.item.key)
        return result[2]
    
def find_min_abs_diff_helper(root, maxa, diff):
    if root.left is None and root.right is None:
        return (root, maxa, diff)
    else:
        val = root.item.key
        left, maxa, diff = find_min_abs_diff_helper(root.left, diff)
        if left.item.key > maxa:
            new_maxa = left.item.key
        new_diff = min(diff, val - left.item.key)
        
        
        right, diff = find_min_abs_diff_helper(root.right, diff) 

        
