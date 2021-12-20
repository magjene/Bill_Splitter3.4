num = int(input('Enter the number of friends joining (including you):\n'))
if num <= 0:
    print('\nNo one is joining for the party')
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    d = {input(): 0 for _ in range(num)}
    bill = round(int(input('\nEnter the total bill value:\n')) / len(d), 2)
    d = {key: bill for key in d}
    print(f'\n{d}')
