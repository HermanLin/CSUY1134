def factors(num):
    for x in range(1, num + 1):
        if num % x == 0:
            yield x

def main():
    for curr_factor in factors(100):
        print(curr_factor, end = ' ')

#main()