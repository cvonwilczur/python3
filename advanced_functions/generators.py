# Generators

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1

g = hundred_numbers()

print([x * 2 for x in hundred_numbers()])

print(next(g)) #prints 0
print(next(g)) #prints 1

# the generator gives you each element of the list
# only remembering the last number
# you have to run the function each time to generate the next number
