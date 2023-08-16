print("teste")

"""
Comments
Comments
Comments
Comments
"""

x = z = y = "banana"

print(z)
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) # apple
print(y) # banana
print(z) # cherry
print("This is the fruits[1]: {}".format(fruits[1]))



def myfunc():
    global x #global variable
    x  = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x) 


import random

print(random.randrange(1, 10)) 

b = "Hello, World!"
# H e l l o ,   W o r l d !
#       9 8 7 6 5 4 3 2 1 0
# [excluded][included] =  [from][to]
print(b[-5:-2]) # this is used to count from the end of string



# H e l l o ,   W o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11 12


print(b[2:5]) # get the especific range of characters of a string [included:excluded] [from:to]
print(b[7])

print(b[2:]) # get the characters of the begin of especified char to the end of string

print("teste 1\nteste 2\nteste 3\taaaa")

a = 14
b = 3

result = a // b

print(result)