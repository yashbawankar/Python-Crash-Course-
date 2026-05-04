my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

friend_foods.append('cannoli')

print("my favourite foods are:")
for food in my_foods:
    print('-',food)

print("\nmy friends favourite foods are:")
for food in friend_foods:
    print('-',food)