
# This is harder assignment, you might check the internet
# Think about solution for few moments
# Note: you can use 'while' loop
# if you are not sure about solution search for 'pseudo code fibonacci sequence'

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.


# 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

# Create a function to generate fibonacci sequence

# if user call fibonacci(5) it should generate '0 1 | 1 2 3 5 8'
# if user call fibonacci(7) it should generate '0 1 | 1 2 3 5 8 13 21'

def fibonacci(length = 2, sequence = None):
    if sequence is None:
        sequence = [0,1]

    if length == 0:
        return sequence

    sequence.append(sequence[-2] + sequence[-1])
    length -= 1

    seq_result = fibonacci(length, sequence)
    return seq_result


fib_result = fibonacci()
print(fib_result)
fib_result = fibonacci(1)
print(fib_result)
fib_result = fibonacci(4)
print(fib_result)
fib_result = fibonacci(7)
print(fib_result)
fib_result = fibonacci(10)
print(fib_result)

