def flat_list(nested_lst, low, high):
    flat = []
    if low == high:
        if isinstance(nested_lst[low], list):
            flat.extend(flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1))
        else:
            return [nested_lst[low]]
    else:
        #print("low: ", low)
        #print("high: ", high)
        if isinstance(nested_lst[low], list):
            flat.extend(flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1))
        else:
            flat.extend([nested_lst[low]])
        flat.extend(flat_list(nested_lst, low + 1, high))
    return flat

#nest_lst = [[1, 2], 3, [4, [5, 6, [7], 8], 9], [10]]
#print(flat_list(nest_lst, 0, 3))