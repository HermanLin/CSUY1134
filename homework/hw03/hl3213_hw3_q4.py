def remove_all(lst, value):
    '''
    end = False
    while end == False:
        try:
            lst.remove(value)
        except ValueError:
            end = True
    '''
    l_lst = len(lst)
    ctr = 0
    for x in range(l_lst):
        if lst[x] != value:
            lst[ctr] = lst[x]
            ctr += 1
    for x in range(ctr, l_lst):
        lst.pop()
    #return lst

#lst = [1,6,3,3,5,8,8,3,4,2,9]
#print(remove_all(lst, 3))