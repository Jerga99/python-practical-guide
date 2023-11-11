
name_1 = 'Filip'
name_2 = 'James'

# names: list[str] = ['Filip', 'James', 'Ema', 'Jess', 'David']

# print(names)
# fruits = list(('apple', 'banana', 'watermelon'))
# print(fruits)
# mix = ['apple', 1, True, 3.14]
# print(mix)


# print(names[2])

# name = names[2]

# print(len(names))

# print(names[1] + names[3])
# print(mix[-1])
# print(mix[-4])

# names: list[str] = ['Filip', 'James', 'Ema', 'Jess', 'David']
# new_names = names[1:4]

# print(names[:4])
# print(names[1:])
# print(names[-4:-1])

# searched_name = input('Please enter a name: ')

# if searched_name in names:
#     print(f'Name {searched_name} is in the list!')
# else:
#     print(f'{searched_name} Not in the list!')


# numbers = [1,3,2,10,9,11]
# i = 0

# while i < len(numbers):
#     print(numbers[i])
#     i+=1

# TODO: Find index of number 10 in the 'numbers' list and print it out


# numbers = [1,3,2,10,9,11]
# i = 0

# while i < len(numbers):
#     if numbers[i] == 10:
#         print(f'Number {numbers[i]} found on index {i}')
#     i+=1


# import random

# numbers = [1,3,2,10,9,11]
# new_numbers =[]
# i = 0

# while i < len(numbers):
#     new_numbers.append(random.randint(900, 999))
#     i+=1

# print(new_numbers)

# numbers = [1,3,2,10,9,11]
# i = 0

# while i < len(numbers):
#     if i % 2 == 0:
#         numbers[i] = random.randint(900, 999)
#     i+=1

# print(numbers)


# names:list[str] = []

# names.append('John')
# names.append('Jess')
# names.append('David')

# print(names)
# names.pop(0)
# print(names)
# names.pop(1)
# print(names)


# names = ['John', 'Jess', 'David', 'Ema']

# found_name = names[50]

# names.append('Rob')

# deleted_name = names.pop(1)
# print(f'I have deleted {deleted_name}')

# del names[-1]

import random

numbers = [1,3,2,10,9,11]
i = 0

while i < len(numbers):
    if i % 2 == 0:
        numbers.pop(i)
    i+=1

print(numbers)

