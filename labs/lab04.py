def str_to_int(n):
    l = len(n)
    intgr = 0
    for x in range(l):
        intgr += int(n[x]) * (10**(l - 1 - x))
    return intgr

def reverse_vowels(input_str):
    lst_str = list(input_str)
    vowels = 'aeiou'
    i, j = 0, len(lst_str) - 1
    stor = ''
    while i < j:
        if lst_str[i] in vowels:
            if lst_str[j] in vowels:
                stor = lst_str[i]
                lst_str[i] = lst_str[j]
                lst_str[j] = stor
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    return lst_str

def jump_search(lst, val, k):
    size = len(lst)
    jmp = 0

    #jumps
    while jmp < size and val > lst[jmp]:
        jmp += k
    #check if reach end of jumps
    if val > lst[jmp]:
        jmp += 1
    else:
        jmp -= k
    #linear search
    

#print(str_to_int("1134"))
#print(reverse_vowels("michellemoe")) #mechollemei
lst = [1,3,6,7,10,12,15,20,22,24,29,33,39,55,61,64,99,101,134,150]
print(jump_search(lst, 15, 4))