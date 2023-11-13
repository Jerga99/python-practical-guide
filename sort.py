

# numbers = [2, 3, 5, 10, 2, 1, 14, 15, 12, 4, 20, 8]
# names = ['Filip', 'Jane', 'Ema', 'Albert', 'David', 'John', 'Lucy']

# numbers.sort(reverse=True)
# names.sort(reverse=True)

# print(numbers)
# print(names)

# def perform_computation(*args, param_one = 'Default 1', param_two = 'Default 2'):

#     for arg in args:
#         print(arg)

#     print(param_one)
#     print(param_two)


# perform_computation(1, 2, 'Filip', 'David', True, False)


# def perform_computation(*, param_one, param_two = 'Default 2'):

#     print(param_one)
#     print(param_two)

# perform_computation(param_one='Hello World')



def perform_computation(*_args, param_one, param_two = 'Default 2'):
    for arg in _args:
        print(arg)

    print(param_one)
    print(param_two)

perform_computation(1,2,3, param_one='Hello World')
