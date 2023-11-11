
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

names: list[str] = ['Filip', 'James', 'Ema', 'Jess', 'David']

print(names[1:4])
print(names[:4])
print(names[1:])
print(names[-4:-1])

searched_name = input('Please enter a name: ')

if searched_name in names:
    print(f'Name {searched_name} is in the list!')
else:
    print(f'{searched_name} Not in the list!')
