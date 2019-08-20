'''

IndexError
- when you call an index that is outside of the range of the iterable

KeyError
- when you call a key of an object that does not exist

NameError
- when you call on a variable that is not defined

AttributeError
- when an attribute does not exist on an object

NotImplementedError
- you can raise this error when a feature is not implemented

RuntimeError
- a base class error that other errors extend out from

SyntaxError
- when you make a mistake in Python syntax

IndentationError
- when you make a mistake in your indexing in Python syntax

TabError
- python doesn't like it when you mix and match indentation types

TypeError
- Attempting to perform unsupported operations on types

ValueError
- when a function is fed an incorrect value

ImportError
- issues with importing

DeprecationWarning
- something you tried to do or use is deprecated

'''

# Raising Errors in Python


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        raise NotImplementedError('We do not have this yet.')


# Creating our own errors

class MyCustomError(TypeError):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

raise MyCustomError('An error has happened!', 500)


# Dealing with errors

def start_car(car):
    try:
        Car.add_car(fiesta)
    except TypeError:
        print('Your car was not a Car!')
    except ValueError:
        raise


