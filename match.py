

option = input('Enter option: ')

# if option == 'left':
#     print('Go Left')
# elif option == 'right':
#     print('Go Right')
# elif option == 'forward':
#     print('Go Forward')
# else:
#     print('Go Backward')

match option:
    case 'left':
        print('Go Left')
    case 'right':
        print('Go Right')
    case 'forward':
        print('Go Forward')
    case _:
        print('Go Backward')
