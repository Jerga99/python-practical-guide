
# name_length = len(f_name) # len('Filip') -> 5
# print(name_length) # 5

# name_character = f_name[0] # 'Filip[0]' -> 'F
# name_character_2 = f_name[2] # 'Filip[0]' -> 'l'
# print(name_character)

# num_1 = 100
# num_2 = 50
# num_3 = 25
# f_name = 'Filip'
# l_name = 'Doe'

# result_1 = (num_2 < num_1) and (num_3 < num_2) and (num_2 > num_1)

# result_2 = (num_1 >= num_2) or (num_3 != num_2) or (num_1 == 100)

# result_3 = (len(f_name) > len(l_name)) and (num_3 <= num_2) and (num_1 != num_2)

# result_4 = (num_1 - num_2) == (num_2 - num_3)

# result_5 = (num_1 / num_2) == 0 or (num_2 / 50) == 1

# result_6 = (num_1 > num_2) and (num_3 < num_1) or (num_2 < num_3)

# result_7 = len(f_name) == len(l_name) and num_2 > 100

# result_8 = f_name[0] == 'F' and l_name[1] == 'o'

# result_9 = len(f_name) + len(l_name) < (num_1 - num_2) * num_3


# print(f'result_1: {not result_1}')
# print(f'result_2: {not result_2}')
# print(f'result_3: {not result_3}')
# print(f'result_4: {not result_4}')
# print(f'result_5: {not result_5}')
# print(f'result_6: {not result_6}')
# print(f'result_7: {not result_7}')
# print(f'result_8: {not result_8}')
# print(f'result_9: {not result_9}')


# 1. Get an input from a user to guess a number

# 2. Generate random number between 1 - 10 (inclusive both) // research how to generate random number

# Create following conditions:
# 3. If the guessed number is the same as the random number and random number is greater than 5 then print out
# 'You are winner with the winning number: {number}

# 4. Number 3 is 'joker' number if you guess the wrong number, but the random number is 3 then you print out
# 'You won the joker.'

# 5. else you print out "You lost"

import random

guess_num = input('Guess number (1-10): ')
rnd_num = str(random.randint(1, 10))

if guess_num == rnd_num and rnd_num > '5':
    print(f'You are winner with number: {rnd_num}')
elif rnd_num == '3':
    print(f'You won the joker with number: {rnd_num}')
else:
    print(f'You lost. Your number is: {guess_num} and winner num is: {rnd_num}')
