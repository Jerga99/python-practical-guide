
# x = 20

# res_1 = x + 5
# res_2 = x - 5
# res_3 = x * 5
# res_4 = x / 5
# res_5 = x ** 2

# res_6 = (res_2 + res_1) * res_4

# print(res_6)

# print(res_1)
# print(res_2)
# print(res_3)
# print(res_4)
# print(res_5)

# # int
# 10
# 15
# -100
# 0

# # float
# 3.14
# 2.85
# 1.2138219739

# # string
# 'Filip Jerga'
# 'Hello World'

# # bool
# True
# False

# result = '10' + '10' # 1010
# result_1 = 'Filip' + ' ' + 'Jerga' # 'Filip Jerga'
# print(result)
# print(result_1)

# bool_result = True + False
# print(bool_result)


# name = 'Filip'
# age = 30
# is_freelancer = True


# name_age = name + str(age) + str(is_freelancer)
# print(name_age)

# # 'Filip is 30 years old, and he is a freelancer: True'

# message = name + ' is ' + str(age) + ' years old, and he is a freelancer: ' + str(is_freelancer)

# print(message)


# x = 10

# sum_1 = x + 100
# print(sum_1)

# # Will not work
# # print(y)

# x = 30
# y = 100
# print(y)

# sum = x + 20
# print(sum)


# a, b, c = 20, 30, 'Filip'

# print(a + b)
# print('Hi ' + c)

# d = e = f = 'Hi There!'

# print(d + e + f)


# Create a variable num1 and num2
# Assign custom numeric values to it (value range between 1-10)
# print out value of num1 to power of num2

num_1 = 5
num_2 = 3

result = num_1 ** num_2
print(result)

# Create variables to hold the information about a dog (name, age, breed, is_injury_free)
# Figure out what data types you want to assign to variables, look at the names
# print out the information about the dog as a one sentence.
# 'Alex is 20 years old, he is german shepard and he is injury free: False'

name = 'Rex'
age = 15
breed = 'German Shepard'
is_injury_free = True

# sentence = name + ' is ' + str(age) + ' years old, he is ' + breed + ' and he is injury free: ' + str(is_injury_free)
# print(sentence)


# sentence = '{1} is {0} years old, he is {2} and he is injury free: {3}'
# sentence = '{} is {} years old, he is {} and he is injury free: {}'

# print(sentence.format(age, name, breed, is_injury_free))
# print('%s is %s years old, he is %s and he is injury free: %s' %(name, age, breed, is_injury_free))

print(f'{name} is {age} years old, he is {breed} and he is injury free: {is_injury_free}')
