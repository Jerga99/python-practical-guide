# Simple Calculator for "addition" "substraction" "multiplication" "division
#                           +            -               *             /

# Create a infinite While loop 
# Inside of this loop ask a user to input the first number
# Inside of this loop ask a user to input the second number

# Inside of this loop ask a user to input one of four options: (+, -, *, /)
#   if user inputs '+' then add numbers and print result
#   if user inputs '-' then substract numbers and print result
#   if user inputs '*' then multiply numbers and print result
#   if user inputs '/' then divide numbers and print result
#   if user inputs any other character or string then start the while loop over and print
#     - 'Wrong Input! Available options are: (+, -, *, /)'

#   Ask user to input 'q' to quit the application 
#   if user inputs 'q' the break the while loop and print 'Application has been closed'

def is_float(text_num: str) -> bool:
    try:
        float(text_num)
        return True
    except ValueError:
        return False

while True:
    x_text = input('Enter first number: ')
    y_text = input('Enter second number: ')

    if not is_float(x_text) or not is_float(y_text):
        print('Please enter numeric values!')
        continue

    x = float(x_text)
    y = float(y_text)

    operation = input('Choose Operation (+, -, *, /): ')
    operation = operation.strip()

    if operation == '+':
        print(f'Result is: {x + y}')
    elif operation == '-':
        print(f'Result is: {x - y}')
    elif operation == '*':
        print(f'Result is: {x * y}')
    elif operation == '/':
        print(f'Result is: {x / y}')
    else:
        print('Wrong Input! Available options are (+, -, *, /)')
        continue

    q_key = input('Press (q) to quit the application, press any other key to continue: ')
    q_key = q_key.strip().lower()

    if q_key == 'q':
        print('Application has been closed!')
        break


