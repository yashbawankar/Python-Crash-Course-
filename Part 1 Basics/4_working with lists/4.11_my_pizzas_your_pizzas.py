# my personal pizzas
pizzas=['Chilly Panner','Cheese Blast',"Flammin Hot"]
# adding a new pizza to my personal pizzas.
pizzas.append('Peperoni Pizza')

# my friend personal pizzas
friend_pizzas=['Chilly Panner','Cheese Blast',"Flam_min Hot"]

# adding a different pizza to my fiend_pizzas.
friend_pizzas.append('7 Cheese')

# prove that, i have two separate lists. print the message
print("My Favourite pizzas are: ")
for pizza in pizzas:
    print("-",pizza)

print("\nMy Friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)

