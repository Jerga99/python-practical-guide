
# This is harder assignment, you might check the internet
# Think about solution for few moments
# Note: you can use 'while' loop
# if you are not sure about solution search for 'pseudo code fibonacci sequence'

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.


# 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

# Create a function to generate fibonacci sequence

# if user call fibonacci(5) it should generate '0 1 | 1 2 3 5 8'
# if user call fibonacci(7) it should generate '0 1 | 1 2 3 5 8 13 21'

def fibonacci(length = 2):
    if length < 0:
        print('Length must be greater than 0!')
        return None

    num_1 = 0
    num_2 = 1
    sequence = '0 1 | '
    i = 0

    while i < length:
        result = num_1 + num_2
        sequence += f'{result} '
        num_1 = num_2
        num_2 = result
        i += 1

    return sequence


fib_result = fibonacci(4)

print(fib_result)

fib_result_2 = fibonacci(-10)

if fib_result_2 is None:
    print("Cannot continue, fibonacci was't generated")
