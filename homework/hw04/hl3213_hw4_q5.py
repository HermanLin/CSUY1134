def count_lowercase(s, low, high):
    count = 0
    if low == high:
        if s[low].islower():
            return 1
    else:
        count += count_lowercase(s, low + 1, high)
        if s[low].islower():
            count += 1
    return count

#s = "zxCKpljwuO" #7
#s1 = "zxCKpljwuo" #8
#print(count_lowercase(s, 0, 9))

def is_number_of_lowercase_even(s, low, high):
    evenOdd = True
    if low == high:
        if s[low].islower():
            return False
        return True
    else:
        evenOdd = is_number_of_lowercase_even(s, low + 1, high)
        if s[low].islower():
            if evenOdd == False:
                evenOdd = True
            else:
                evenOdd = False
    return evenOdd
        

#False
#print(is_number_of_lowercase_even(s, 0, 9))
#True
#print(is_number_of_lowercase_even(s1, 0, 9))