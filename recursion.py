
r = 0

print('Start of the program')

def recursion():
    global r
    print(f'Hello recursion r - {r}')

    if r == 3:
        print('Returning from recursion')
        return None

    r += 1
    recursion()
    print('Hi There')
    return None

recursion()

print('End of the program')
