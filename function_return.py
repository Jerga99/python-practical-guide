'''This module show how to return the values from functions'''

testing = 100


# '''Function that runs learning content code'''
def add(num_1, num_2):
    '''Function adding two numbers together and returning the result'''
    return num_1 + num_2

result = add(10, 20)
print(f'RESULT: {result}')
add(100, 200)
print(f'RESULT: {result}')



def welcome(name):
    '''Function returning welcome message joined by (name) parameter'''
    msg = f'Welcome {name}'
    return msg


print(welcome('Filip'))
print(welcome('Jess'))



def nice_function(x: int, y: float, print_message: str, should_increment = True) -> float:
    '''
    Nobody know what this function does
        Paramters:
            x (int): First multiplication value
            y (float): Second multiplication value
            print_message (str): Message that will be printed out
            should_increment (bool): When True, inrements result by 10
        Returns:
            Returns the result of multiplication
    '''
    sum_result = x + y

    if should_increment:
        sum_result *= 10

    print(f'{print_message}{result}')

    return sum_result


result = nice_function(10, 2.82, 'Result is: ')
print(result)
