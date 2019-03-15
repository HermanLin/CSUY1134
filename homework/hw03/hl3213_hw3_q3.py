def find_duplicates(lst):
    dups = []
    len_lst = len(lst)
    for i in range(len_lst):
        if lst[abs(lst[i])] >= 0:
            lst[abs(lst[i])] = - lst[abs(lst[i])]
        else:   
            dups.append(abs(lst[i]))
    return dups

lst = [2, 3, 2, 8, 1, 0, 0, 9, 0, 7]
print(find_duplicates(lst))