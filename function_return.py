

def add(num_1, num_2):
    result = num_1 + num_2
    return result

result = add(10, 20)
print(result)


def welcome(name):
    msg = f'Welcome {name}'
    return msg


print(welcome('Filip'))
print(welcome('Jess'))



def nice_function(x: int, y: float, print_message: str, should_increment = True) -> float:
    result = x + y

    if should_increment:
        result *= 10

    print(f'{print_message}{result}')

    return result


result = nice_function(10, 2.82, 'Result is: ')
print(result)




