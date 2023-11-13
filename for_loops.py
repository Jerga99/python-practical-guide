

names = ['Eli', 'Martin', 'John', 'Jane']

# i = 0
# while i < len(names):
#     print(names[i])
#     i+=1

# for x in names:
#     print(x)

# for name in names[1:3]:
#     print(name)

# for name in names:
#     for letter in name:
#         print(letter)
#     print(name)

# for name in names:
#     if name == 'John':
#         break
#     print(name)


# for name in names:
#     if name == 'John':
#         continue
#     print(name)

for name in names:
    for letter in name:
        if letter == 'J':
            continue
        print(letter)
    print(name)
