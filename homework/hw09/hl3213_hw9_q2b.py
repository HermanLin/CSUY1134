from ChainingHashTableMap import ChainingHashTableMap

#best average case runtime: O(min(len(lst1), len(lst2)))
def intersection_list(lst1, lst2):
    '''
    if len(lst1) <= len(lst2):
        smol, bigr = lst1, lst2
    else:
        smol, bigr = lst2, lst1
    result = []
    for i in smol:
        if i in bigr:
            result.append(i)
    return result
    '''
    table = ChainingHashTableMap()
    result = []
    for i in lst1:
        try:
            table[i] += 1
        except:
            table[i] = 1
    for j in lst2:
        try:
            table[j] += 1
        except:
            table[j] = 1
    for k in table:
        if table[k] > 1:
            result.append(k)
    return result
