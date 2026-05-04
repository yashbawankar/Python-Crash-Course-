usernames=['oggy','jack','admin','dee dee','joe']

for username in usernames:
    if 'admin' in username:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")