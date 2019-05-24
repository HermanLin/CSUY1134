from BinarySearchTreeMap import BinarySearchTreeMap

#===== 2a =====#
#RUNTIME: THETA(N^2)
#You are inserting each
def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for k in range(n):
        bst[k + 1] = None
    return bst

#===== 2b =====# RUNTIME: 
def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == high:
        bst[low] = None
    else:
        mid = (high + low) // 2
        bst[mid] = None
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)
