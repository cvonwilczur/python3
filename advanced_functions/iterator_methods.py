# filter

# python is one of the few programming languages that has list comprehensions
# so sometimes using filter is advantageous for developers new to Python

def starts_with_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Jose']

start_with_r = filter(starts_with_r, friends)

# map

friends_lower = map(lambda x: x.lower(), friends)

# any evaluates true if any item in the iterable evaluates to true
# all evalutes to true if all item in the iterable evaluates to true


# enumerate is for when you want to iterate over something and want the index

for i, friend in enumerate(friends):
    print(f'My top {i + 1} friend is {friend}')
