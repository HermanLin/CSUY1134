def appearances(s, low, high):
    count_dict = {}
    if low == high:
        if s[low] in count_dict:
            count_dict[s[low]] += 1
        else:
            count_dict[s[low]] = 1
    else:
        count_dict = appearances(s, low + 1, high)
        if s[low] in count_dict:
            count_dict[s[low]] += 1
        else:
            count_dict[s[low]] = 1
    return count_dict

#print(appearances("Hello world", 0, 10))