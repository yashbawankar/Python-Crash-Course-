current_users=['oggy','jack','bob','marky','joe']

new_users=['dee dee','OggY','tom','peter','BoB']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} is exits, A person will need to enter a new username.")
    else:
        print(f"{new_user} username is available.")