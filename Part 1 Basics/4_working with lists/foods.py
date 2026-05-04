#copying a list
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print("my favourite foods are:")
print(my_foods)

print("my friends favourite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favourite foods are:")
print(my_foods)

print("\nmy friends favourite foods are:")
print(friend_foods)