
# MUTABLE
items = ['Filip', 'Jess', 'Peter', 'Ema']

# IMMUTABLE
person = ('Filip', 32, 'Slovakia', True)
# person = tuple(('Filip', 32, 'Slovakia', True))
# person: tuple[str, int, str, bool] = ('Filip', 32, 'Slovakia', True)


for prop in person:
    print(prop)

# print(person[3])

new_person = (person[0], person[1], 'Germany', False)

print(person)
print(new_person)


new_items = items

new_items[2] = 'WHATEVER'

print(items)
print(new_items)


def whatever():
    return (True, 'Filip')
