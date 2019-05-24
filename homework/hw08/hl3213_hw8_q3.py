from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    mini = min(prefix_lst)
    size = len(prefix_lst) - 1
    bst.root = restore_bst_helper(prefix_lst, mini, prefix_lst[size], 0)
    return bst

def restore_bst_helper(lst, mini, maxa, index):
    if index == len(lst):
        return None
    else:
        item = BinarySearchTreeMap.Item(lst[index])
        new_node = BinarySearchTreeMap.Node(item)
        if lst[index] >= mini and lst[index] <= maxa:
            new_node.left = restore_bst_helper(lst, mini, item.key, index + 1)
        elif lst[index] >= mini and not lst[index] <= maxa:
            new_node.right = restore_bst_helper(lst, item.key, lst[index - 1], index + 1)
        else:
            new_node.right = restore_bst_helper(lst, item.key, maxa, index + 1)
        return new_node
        
