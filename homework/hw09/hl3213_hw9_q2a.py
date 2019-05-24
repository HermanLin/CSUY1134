

#best worst case runtime: O(len(lst1) * len(lst2))
def intersection_list(lst1, lst2):
    '''
    result = []
    for i in lst1:
        for j in lst2:
            if i == j:
                result.append(i)
    return result
    '''
    lst1.sort()
    lst2.sort()
    p1 = 0
    p2 = 0
    result = []
    while len(lst1) > p1 and len(lst2) > p2:
        if lst1[p1] == lst2[p2]:
            result.append(lst1[p1])
            p1 += 1
            p2 += 1
        elif lst1[p1] > lst2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result
