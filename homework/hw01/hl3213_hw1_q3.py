#sum_squared_a(n)
#pre: int
#post: int
#returns the sum of the squares of all (+) int < n
def sum_squared_a(n):
    ret = 0
    for i in range(n):
        ret += i**2
    return ret

#sum_squared_b(n)
#pre: int
#post: int
#uses list comprehension to return the sum of the squares of all (+) int < n
def sum_squared_b(n):
    return sum([i**2 for i in range(n)])

#sum_squared_c(n)
#pre: int
#post: int
#returns the sum of the squares of all odd (+) int < n
def sum_squared_c(n):
    ret = 0
    for i in range(n):
        if i % 2 == 1:
            ret += i**2
    return ret

#sum_squared_d(n)
#pre: int
#post: int
#uses list comprehension to return the sum of the squares of all odd (+) int < n
def sum_squared_d(n):
    return sum([i**2 for i in range(n) if i % 2 == 1])