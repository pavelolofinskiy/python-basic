def print_max(x, y):
    '''Print the maximum of two numbers.
The two values must be integers.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print(print_max.__doc__)
print_max(input('First number'), input('Second number'))
