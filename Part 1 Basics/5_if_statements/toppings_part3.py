
requested_toppings=['mushrooms','extra cheese','pepperoni']

# using if else inside for loop
for requested_topping in requested_toppings:
    if requested_topping == 'pepperoni':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished Making Your Pizza!")