from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

'''
def permutations(lst):
    temp = [0] * len(lst)
    q = ArrayQueue()
    q.enqueue(lst)

    i = 1
    while i < len(lst):
        if temp[i] < i:
            if i % 2 == 0:
                j = temp[i]
            else:
                j = 0
            lst[j], lst[i] = lst[i], lst[j]
            q.enqueue(lst)
            temp[i] += 1
            i = 1
        else:
            temp[i] = 0
            i += 1
    for x in range(len(q)):
        print(q.dequeue())
    #return q.data
'''

def permutations(lst):
    perms = ArrayStack()
    parts = ArrayQueue()
    combo = []

    for x in range(len(lst)):
        if perms.is_empty():
            perms.push([lst[x]])
        else:
            for y in range(len(perms)):
                p_lst = perms.pop()
                for z in range(len(p_lst) + 1):
                    parts.enqueue(p_lst[:z] + [lst[x]] + p_lst[z:])
            for a in range(len(parts)):
                perms.push(parts.dequeue())
    while not perms.is_empty():
        combo.append(perms.pop())
    return combo
    
def main():
    lst = [1,2,3]
    print(permutations(lst))

#main()