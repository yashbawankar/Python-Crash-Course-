# creating a list of available toppings
available_toppings=['mushrooms','olive','green peppers','pepperoni','pineapple','extra cheese']

# requested toppings by customer
requested_toppings=['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished Making your Pizza!.")