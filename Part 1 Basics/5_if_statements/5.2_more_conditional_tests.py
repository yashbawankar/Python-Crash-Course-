#tests for equality and inequality with strings
# equality.
print("Equality")
car='subaru'
if car == 'subaru':
    print("Checking equality:",car)
print()
# inequality.
print("Inequality")
car='Honda'
if car != 'subaru':
    print("Checking inequality:",car)
print()
# using lower()
print("Using lower()")
car='Audi'
if car.lower() == 'audi':
    print("I have Car named:",car)
print()
# Numerical tests.
# 1 case equality.
print("Case 1")
num = 55
if num == 55:
    print(num)
print()

# case 2 inequality.
print("Case 2")
if num != 54: # change the number value to switch cases.
    print("different number")
else:
    print("same number")
print()

# case 3 greater than and less than
print("Case 3")
a,b=5,4
if (a>b) and (b<a):
    print("a greater than and less than.")
else:
    print("b greater than and less than.")
print()

# case 4 greater than or equal to.
print("Case 4")
a,b=1,1
if (a>b) or (a==b):
    print("a greater than or equal to.")
else:
    print("b greater than or equal to.")
print()

# case 5 less than or equal to.
print("Case 5")
a,b=5,1
if (a<b) or (a==b):
    print("a is less than or equal to.")
else:
    print("b is less than or equal to.")
print()

# tests using and keyword, or keyword using a list.

fruits=['banana','apple','pineapple','strawberry']
# case 1 using in operator.
fruit='apple'
if fruit in fruits:
    print("on the fruits list",fruit)
else:
    print("not in a list")

# Case 2 using and keyword.
fruit = 'apple' and 'banana'
if fruit in fruits:
    print("on the fruits list")
else:
    print("not in a list")

# Case 3 using or keyword.
fruit = 'apple' or 'pineapple'
if fruit in fruits:
    print("on the fruits list")
else:
    print("not in a list")