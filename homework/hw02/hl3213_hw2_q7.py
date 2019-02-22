def findChange(lst01):
    ctr = 0
    while lst01[ctr] != 1:
        ctr += 1
    return ctr

def main():
    lst = [0,0,0,0,0,1,1,1]
    findChange(lst)

#main()