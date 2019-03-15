def ss(lst, low, high):
    if low == high:
        print("basecase:",lst[low])
        return lst[low]
    else:
        print("list[low]: ", lst[low])
        return lst[low] <= ss(lst, low + 1, high)

lst1 = [1, 3, 6, 8, 12, 15, 31]
lst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ss(lst1, 0, 6))