import random

n1 = int(input("first number:"))
n2 = int(input("second number:"))

random_num = random.randrange(n1,n2)


print("A number between {} and {} : {}".format(n1,n2,random_num))

