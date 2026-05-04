motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
# ['honda', 'yamaha', 'suzuki']
motorcycles[0]='ducati'
print(motorcycles)
# ['ducati', 'yamaha', 'suzuki']

# appending elements.
motorcycles.append('honda')
print(motorcycles)

# inserting elements.
motorcycles.insert(0,'BMW')
print(motorcycles)

# Deleting Elements.
print(motorcycles)
del motorcycles[4]
print(motorcycles)

# pop()
print("pop()")
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# removing an item by value.

print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)