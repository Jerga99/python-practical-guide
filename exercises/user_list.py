# 1. Create list of user names, with initial values ['John', 'Peter']
# 2. Create 4 functions - 
#       - add_user -> adds new name to the user list
#       - remove_user -> removes a name from the user list
#       - move_user -> move a user from one position to another in the list
#       - print_users -> print all users in the list

# 3. Create Infinite While Loop
# 4. Inside of the while loop ask user to input 4 options
#       - 'a' -> to add user
#       - 'r' -> to remove user
#       - 'm' -> to move user
#       - 'p' -> to print user list

# 5. After selection a specific option ask user to provide:
#    'name' (if add or remove was selected), and add or remove user
#    'from_idx', 'to_idx' (if move user was select), also display list after operation

# 6. If user inputs 'q' then quit the while loop

# Note: you don't need to implement any safe checks, just focus on functionality


all_users = ['John', 'Peter']

def add_user(name: str):
    all_users.append(name)

def remove_user(name: str):
    all_users.remove(name)

def move_user(source_name: str, target_name: str):
    to_idx = all_users.index(source_name)
    from_idx = all_users.index(target_name)

    temp_name = all_users[to_idx]
    all_users[to_idx] = all_users[from_idx]
    all_users[from_idx] = temp_name

def print_users():
    print(all_users)

while True:
    option = input('a - add, r - remove, m - move, p - print, q - quit: ')

    if option == 'a':
        name_to_add = input('Write name: ')
        add_user(name_to_add)
    elif option == 'r':
        name_to_remove = input('Write name: ')
        remove_user(name_to_remove)
    elif option == 'm':
        initial_name = input('Select initial name: ')
        final_name = input('Switch position with name: ')
        move_user(initial_name, final_name)
    elif option == 'p':
        print_users()
    elif option == 'q':
        break
