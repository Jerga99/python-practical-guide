

# num_1 = 10
# num_2 = 10

# result_1 = num_1 < num_2
# result_2 = num_1 > num_2
# result_3 = num_1 == num_2
# result_4 = num_1 <= num_2 # small or equal
# result_5 = num_1 >= num_2 # greater or equal

# print(f'Result 1: {result_1}')
# print(f'Result 2: {result_2}')
# print(f'Result 3: {result_3}')
# print(f'Result 4: {result_4}')
# print(f'Result 5: {result_5}')

# num_1 = 20
# num_2 = 10
# num_3 = 10

# result = num_1 > num_2

# if num_1 > num_2: print('How are you?')
    
# print('Hi There!')
# print('Hello There')

# num_1 = 20
# num_2 = 10
# num_3 = 100

# if num_1 > num_2:
#     print('Do one thing')
# else:
#     print('Something!')

# if num_2 < num_1:
#     print('Do other thing')
# elif num_1 == num_3:
#     print('Something else!')
# else:
#     print('Hola!')

# if num_3 < 100:
#     print('Num 3 < 100')
# else:
#     print('Do last thing')

# if num_1 < num_2:
#     print('Do one thing')
# elif num_2 == num_3:
#     print('Do other thing')
# elif num_3 < 1000:
#     print('Num 3 < 100')
# else:
#     print('Do last thing')


# name_1 = 'John'
# name_2 = 'JohN'

# result = name_1 != name_2

# if name_1 != name_2:
#     print('Names are NOT the same')
# else:
#     print('Names are the same')

num_1 = 10
num_2 = 20
num_3 = 30

result_1 = (num_2 < num_1) and (num_3 < num_2) and (num_2 > num_1)
result_2 = ((num_2 < num_1) and (num_3 < num_2)) or (num_2 > num_1)
result_3 = (num_2 > num_1) and (num_3 > num_2) and (num_2 > num_1)
result_4 = ((num_2 > num_1) and (num_3 > num_2)) and (num_2 > num_1)
result_5 = ((num_2 > num_1) and (num_3 > num_2)) and (num_2 < num_1)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)




