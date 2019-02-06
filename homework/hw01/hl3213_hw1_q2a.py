#shift(lst, k)
#pre: arr, int
#post: arr
#shifts numbers in lst k indicies to the left
def shift(lst, k):
    while k > 0:
        stor = lst[0]
        for i in range(len(lst) - 1):
            lst[i] = lst[i + 1]
        lst[len(lst) - 1] = stor
        k -= 1
    return lst