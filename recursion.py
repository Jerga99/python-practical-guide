
# r = 0

# print('Start of the program')

# def recursion():
#     global r
#     print(f'Hello recursion r - {r}')

#     if r == 3:
#         print('Returning from recursion')
#         return None

#     r += 1
#     recursion()
#     print('Hi There')
#     return None

# recursion()

# print('End of the program')


print('Start of the program')

def recursion(num: int):
    print(f'Hello recursion r - {num}')

    if num == 3:
        print('Returning from recursion')
        return num

    result = recursion(num+1)
    print(f'Result - {result}')
    return result - 1

last_result = recursion(1)
print(f'Result - {last_result}')

print('End of the program')
