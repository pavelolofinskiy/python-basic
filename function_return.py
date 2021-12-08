def maximum(x, y):
    if x > y:
        return x, 'is higher'
    elif x == y:
        return 'The numbers are equal!!'
    else:
        return y,'is higher'

print(maximum(input("First number"), input("Second number")))