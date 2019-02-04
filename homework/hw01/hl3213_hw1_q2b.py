def shift(lst, k, s = "left"):
    if s == "left":
        for x in range(k):
            stor = lst[0]
            for i in range(len(lst) - 1):
                lst[i] = lst[i + 1]
            lst[len(lst) - 1] = stor
    elif s == "right":
        for x in range(k):
            stor = lst[len(lst) - 1]
            for i in range(len(lst) - 1):
                lst[len(lst) - 1 - i] = lst[len(lst) - 2 - i]
            lst[0] = stor
    return lst