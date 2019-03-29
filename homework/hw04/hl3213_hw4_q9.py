def permutations(lst, low, high):
    perm_lst = []
    if low == high:
        return lst[low]
    else:
        for x in lst:
            perm = [y for y in lst if y != x]
            z = permutations(perm, low, high - 1)
            #perm_lst.append(x)
            if isinstance(z, list):
                for e in z:
                    perm_lst.append([e])
            else:
                perm_lst.append(x)
    return perm_lst


p_lst = [1, 2, 3]
print(permutations(p_lst, 0, 2))