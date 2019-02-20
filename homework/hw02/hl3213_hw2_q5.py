def split_parity(lst):
    l, r = 0, len(lst) - 1
    stor = 0
    #print(lst)

    while l <= r:
        #print(str(l) + ", " + str(r)
        if lst[l] % 2 == 0:
            if lst[r] % 2 == 1:
                stor = lst[l]
                lst[l] = lst[r]
                lst[r] = stor
            else:
                r -= 1
        else:
            l += 1
    return lst

def main():
    split_parity([1,2,3,4])
    split_parity([1,5,2,8,4,7,6,3,9])

#main()