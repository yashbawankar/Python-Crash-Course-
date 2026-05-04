# creating a tuple.
buffet=('Roti','Sabzi','Dal','Chawal','Pappad')
print("Buffet Items are: ")
# use a for loop to print each food
for item in buffet:
    print('-',item)

# try to modify one of the items
#buffet[0]='boti'
# it gets an error cause tuple are immutable.

# changing menu replacing two of the items with diff foods.
print("Changing The Buffet Menu..")
buffet=('Roti','Sabzi','Biryani','Sambhar','Pappad')
for item in buffet:
    print('-',item)