from LinkedBinaryTree import LinkedBinaryTree

opr = "+-*/"

def create_expression_tree(prefix_exp_str):
    expr = prefix_exp_str.split(" ")
    def create_expression_tree_helper(prefix_exp, start_pos):
        elem = expr[start_pos]
        if elem not in opr:
            return LinkedBinaryTree.Node(elem)
        else:
            left = LinkedBinaryTree.Node(elem)
            prefix_exp.left = create_expression_tree_helper(left, start_pos + 1)
            right = LinkedBinaryTree.Node(elem)
            prefix_exp.right = create_expression_tree_helper(right, start_pos + 2)
            return prefix_exp
        
    root = LinkedBinaryTree.Node(expr[1])
    return LinkedBinaryTree(create_expression_tree_helper(root, 0))
        
