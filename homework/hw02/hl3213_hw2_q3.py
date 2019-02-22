import math

def factors(num):
    sq = math.ceil(math.sqrt(num))
    for x in range(1, sq):
        if num % x == 0:
            yield x
    for y in range(sq, 0, -1):
        if num % y == 0:
            yield int(num / y)

def main():
    for curr_factor in factors(100):
        print(curr_factor, end = ' ')

#main()