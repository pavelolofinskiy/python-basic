number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratulations!! You guess it.')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done')