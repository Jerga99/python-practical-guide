print('Program is Starting!')

x = 10
y = 20
z = 30

def a():
    x = 200
    x += 100
    z = 300
    result = x + z
    new_val = 'Hi There'

    if result > 200:
        print('You made it!')
        print(new_val)
        another_val = 42

    result += another_val
    print(another_val)
    print(result)

result = 20 + z
print(result)
age = 33
x += 20

def b():
    a()
    x = 200
    print(x)

    # Why it wont work?
    global result
    print(result)
    result += 30

    print('Nothing new to see here')
    
    def bb():
        print('BB')

        # Why it wont work? Try global/nonlocal
        global x
        x += 20
        print(x)

    bb()
    
    age = 21

    # will not work
    # c(name='Frederik', 23)

    # c('Frederik', 30)
    c('Frederik', age=age)

# Why it wont work?
# print(cc)

def c(name, age):
    print('Hey! I am C!')
    text = 'I am just text'

    # What is this?
    global aa
    aa = 20

    bb = 30
    global cc
    cc = 40

    if len(name) > 6:
        print('You have very long name!')

        some_var = 'Hmmm'

        if age < 20:
            print('You are really young!')
            print(some_var)
            some_var_2 = 100

        print('Out of here!')

        # Why error here?
        # print(some_var_2)
    
    print(text)

b()

print(aa)

# Will not work?
# print(bb)
print(cc)

print('Program End')
