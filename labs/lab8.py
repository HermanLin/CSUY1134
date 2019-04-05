def is_balanced(inp_str):
    lefty = "([{"
    righty = ")]}"
    tmp_stack = ArrayStack()
    for i in inp_str:
        if i is.in lefty:
            tmp_stack.push()
        else:
            #is of same type as stack.top()
            #if not, return false