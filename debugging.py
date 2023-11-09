
name = 'Filip'
age = 32

def print_user_info(name, age, age_in_days = False, birthplace = 'Earth'):
    age_measure = 'years'

    if age_in_days:
        age_measure = 'days'
        age *= 365

    print(f'Birthplace is: {birthplace}')
    print(f'{name} is {age} {age_measure} old')

print_user_info('John', age=age, age_in_days=True, birthplace='Norway')
print_user_info('Filip', age=age, age_in_days=False)
print_user_info(name=name, age=age)
print_user_info(name='Ema', age=50)
print_user_info(name='Julia', age=33, birthplace='Germay')
print_user_info(name='David', age=40, age_in_days= False)
