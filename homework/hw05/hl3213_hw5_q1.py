from ArrayStack import ArrayStack

opr = "+-*/"
not_done = True
pfix = ArrayStack()
vars = {}

def eval_postfix(expr):
    #print(expr)
    for ops in expr:
        #print(ops)
        if ops not in opr:
            if ops in vars:
                pfix.push(vars.get(ops))
            else:
                pfix.push(str_to_num(ops))
        else:
            val1 = pfix.pop()
            val2 = pfix.pop()
            if ops == opr[0]:
                pfix.push(val2 + val1)
            elif ops == opr[1]:
                pfix.push(val2 - val1)
            elif ops == opr[2]:
                pfix.push(val2 * val1)
            elif ops == opr[3]:
                pfix.push(val2 / val1)
    return(pfix.pop())

def var_assign(expr):
    variable, expr = expr.split(" = ")
    expr = expr.split(" ")
    #print(expr)
    vars[variable] = eval_postfix(expr)
    #print("vars dict:", vars)
    return variable

def str_to_num(string):
    if string.isdigit():
        return int(string)
    else:
        return float(string)

while not_done:
    exp = input("-->")
    if exp == "done()":
        not_done = False
    else:
        if "=" in exp:
            print(var_assign(exp))
        else:
            exp = exp.split(" ")
            print(eval_postfix(exp))
