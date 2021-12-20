"""
Project Bill Splitter. Stage 2/4.

It's bill time! Let's split the bill among everyone and update the values in the dictionary
you have created in the previous stage.
Since we don't want to deal with too many decimals (who carries that much change anyway?),
round the split amount to two decimal places and then update the dictionary with the split values.

Objectives
In this stage your program should perform the following steps together with the steps of the previous stage:
If there are no people to split the bill (the number of friends is 0 or an invalid input),
output "No one is joining for the party";
Else, take user input: the final bill;
Split the total bill equally among everyone;
Round the split value to two decimal places;
Update the dictionary with the split values;
Print the updated dictionary.
Do not print the output of the previous stage (see examples).

Examples
The greater-than symbol followed by a space (> ) represents the user input.
Note that it's not part of the input.

Example 1: Five people joining

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

{'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}
Example 2: Seven people joining

Enter the number of friends joining (including you):
> 7

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason
> Ben
> Ned

Enter the total bill value:
> 41

{'Marc': 5.86, 'Jem': 5.86, 'Monica':5.86, 'Anna': 5.86, 'Jason': 5.86, 'Ben': 5.86, 'Ned': 5.86}
Example 3: Invalid input

Enter the number of friends joining (including you):
> 0

No one is joining for the party
"""
num = int(input('Enter the number of friends joining (including you):\n'))
if num <= 0:
    print('\nNo one is joining for the party')
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    d = {input(): 0 for _ in range(num)}
    bill = round(int(input('\nEnter the total bill value:\n')) / len(d), 2)
    d = {key: bill for key in d}
    print(f'\n{d}')
