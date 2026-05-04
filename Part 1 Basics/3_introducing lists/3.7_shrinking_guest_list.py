# shrinking guest list.
print("I only invite two people for dinner.")
invitation=['DeeDee','Olly','Joe','Oggy','Jack','Marky']
first_guest=invitation.pop(0)
print(f"Sorry I can't invite {first_guest.title()} to a dinner.")
second_guest=invitation.pop(0)
print(f"Sorry I can't invite {second_guest.title()} to a dinner.")
third_guest=invitation.pop(0)
print(f"Sorry I can't invite {third_guest.title()} to a dinner.")
fourth_guest=invitation.pop(2)
print(f"Sorry I can't invite {fourth_guest.title()} to a dinner.")

# remaining one still invited.
print(f"you're still invited {invitation[0].title()}")
print(f"you're still invited {invitation[1].title()}")

# using del to remove last two names.
del invitation[0]
del invitation[0]
# empty list
print(invitation)