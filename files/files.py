my_file = open('data.txt', 'r')

file_content = my_file.read()

my_file.close()

print(file_content)

my_file_writing = open('data.txt', 'w')

my_file_writing.write('blah')

my_file_writing.close()

# reading csv files

dnd_file = open('csv_data.txt', 'r')

dnd_lines = dnd_file.readlines()

dnd_file.close()

dnd_lines = [line.strip() for line in dnd_lines[1:]]

for line in dnd_lines:
    person_data = line.split(',')
    name = person_data[0]
    race = person_data[1]
    _class = person_data[3]


# reading json files
import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)

file.close()


# using the with syntax
with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file) #reads file and turns it into a dict