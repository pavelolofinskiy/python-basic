adress_book =  {
    'Swaroop': 'swaroop@gmail.com',
    'Larry': 'larry@gmail.com',
    'Matsumoto': 'matz@gmail.com',
    'Spammer': 'spammer@gmail.com'
}

print("Swaroop's adress is", adress_book['Swaroop'])

del adress_book['Spammer']

print('\nThere are {} contacts in the adress-book\n'.format(len(adress_book)))

for name, adress in adress_book.items():
    print('Contact {} at {}'.format(name, adress))

adress_book['Guido'] = 'guido@python.org'
if 'Guido' in adress_book:
    print("\nGuido's adress is", adress_book['Guido'])