def split_by_sign(lst, low, high):
    stor = 0
    if low == high:
        stor = lst[low]
        lst[low] = lst[high]
        lst[high] = stor
    else:
        if lst[low] >= 0:
            if lst[high] < 0:
                stor = lst[low]
                lst[low] = lst[high]
                lst[high] = stor  
                split_by_sign(lst, low + 1, high)
            else:
                split_by_sign(lst, low, high - 1)     
        else:
            split_by_sign(lst, low + 1, high)
    return lst

#test = [5, -5, -4, 9, -7, -1]
#print(split_by_sign(test, 0, 5))
#lst = [5, -5, -4, 9, -7, -1, -3, 2, -9, 3]
#print(split_by_sign(lst, 0, 9))