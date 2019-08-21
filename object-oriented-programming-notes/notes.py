# objects contain data

class Student:
    # special dunder functions, dunder init
    def __init__(self, new_name, new_grades):
        # these are called object properties
        self.name = new_name
        self.grades = new_grades

    # this is called an object method
    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70, 88, 90, 99])

# magic methods
# pretty much everything in python is an object, and has special dunder methods

# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # optional
    def __len__(self):
        return len(self.players)

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
    def __getitem__(self, i):
        return self.players[i]

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object
    def __repr__(self):
        return 'Club {}: {}'.format(self.name, self.players)

    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object
    def __str__(self):
        return 'Club {} with {} players'.format(self.name, len(self))



# static and class methods
    class Foo:
        @classmethod
        def hi(cls):
            print(cls.__name__)

    my_object = Foo()
    my_object.hi() # prints out Foo

    class Bar:
        @staticmethod
        def hi():
            print('Hello, I dont take parameters')

        another_object = Bar()
        another_object.hi()
