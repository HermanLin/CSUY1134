#fibs(n)
#pre: int
#post: arr
#returns a generator that contains the first n elements in the Fibonacci sequence
def fibs(n):
    curr, prev, stor = 1, 1, 0
    while n > 0:
        yield prev
        stor = curr
        curr += prev       
        prev = stor 
        n -= 1