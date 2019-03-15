def count_lowercase(s, low, high):
    ctr = 0
    if low == high:
        if s[low].islower():
            ctr += 1
    else:
        return ctr + count_lowercase(s, low + 1, high)


s = "LZibRfVnhi"
print(count_lowercase(s, 3, 3))