def shift(lst, k):
    for x in range(k):
        stor = lst[0]
        for i in range(len(lst) - 1):
            lst[i] = lst[i + 1]
        lst[len(lst) - 1] = stor
    return lst