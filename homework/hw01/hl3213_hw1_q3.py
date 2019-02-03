def sum_squared_a(n):
    ret = 0
    for i in range(n):
        ret += i**2
    return ret

def sum_squared_b(n):
    return sum([i**2 for i in range(n)])

def sum_squared_c(n):
    ret = 0
    for i in range(n):
        if i % 2 == 1:
            ret += i**2
    return ret

def sum_squared_d(n):
    return sum([i**2 for i in range(n) if i % 2 == 1])