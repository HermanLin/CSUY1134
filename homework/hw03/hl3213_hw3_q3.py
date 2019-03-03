def find_duplicates(lst):
    dups = []
    len_lst = len(lst)
    for i in range(len_lst):
        if lst[abs(lst[i])] >= 0:
            lst[abs(lst[i])] = - lst[abs(lst[i])]
        else:   
            dups.append(abs(lst[i]))
    return dups

#lst = [2,4,4,1,2]
#print(find_duplicates(lst))