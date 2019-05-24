from BinarySearchTreeMap import BinarySearchTreeMap

bst = BinarySearchTreeMap()

bst[9] = 9
bst[7] = 7
bst[3] = 3
bst[1] = 1
bst[5] = 5
bst[13] = 13
bst[11] = 11
bst[15] = 15

for i in iter(bst):
    print(i, end = " ")
print("")

bst[6] = None

for i in iter(bst):
    print(i, end = " ")
    
print(bst[6])

    
