def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        return min(lst[low], list_min(lst, low + 1, high))

#lst1 = [2,9,4,8,6,3,1,5,7,0]
#print(list_min(lst1, 3, 7))