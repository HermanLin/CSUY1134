#use list comprehension to produce [1,10,100,1000,10000,100000]
print([10**i for i in range(6)])
#use list comprehension to produce [0,2,6,12,20,30,42,56,72,90]
print([i**2 + i for i in range(10)])
#use list comprehension to produce ['a','b','c',...,'z']
print([chr(i) for i in range(97, 123)])