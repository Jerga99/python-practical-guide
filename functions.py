


name = 'Filip'
age = 32

name_2 = 'Lucy'
age_2 = 29

# print(f'{name} is {age} years old')
# print(f'{name_2} is {age_2} years old')

def print_user_info(name, age, age_in_days = False):
    age_measure = 'years'

    if age_in_days:
        age_measure = 'days'
        age *= 365

    print(f'{name} is {age} {age_measure} old')


print_user_info('Mark', 45, True)
print_user_info('John', 200)

print_user_info('Alena', 23, True)
print_user_info('Jess', 25, False)

print_user_info(name, age)
print_user_info(name_2, age_2, True)



