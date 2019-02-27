'''8-1. Message: Write a function called display_message() that prints one sen-
tence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.'''


def display_message():
    print("I'm learning about functions in this chapter.")

display_message()


'''8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title . The function should print a message, such as One of my
favorite books is Alice in Wonderland . Call the function, making sure to
include a book title as an argument in the function call.'''


def favorite_book(title):
    print(f"My favorite book is {title}.")


favorite_book("the Magician")

'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''

def make_shirt1(**kwargs):

    for k,v in kwargs.items():
        if k == "size":
            size = v
        if k == "message":
            message = v

    print(f"The size you ordered is {size}.\n"
          f"The following message will be printed on the T-shirt: {message}")


make_shirt1(size ="XL", message = "I'm huge, man!")

'''8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.'''

def make_shirt2(size = "Large", message = "I love Python."):

    print(f"The size you ordered is {size}.\n"
          f"The following message will be printed on the T-shirt: {message}")


make_shirt2()
make_shirt2(size="Medium")
make_shirt2(message='Hoobaaaaaa')

'''8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland . Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.'''


def describe_city(city, country = "the Netherlands"):
    print(f'The city {city} is located in the country of {country}.')

describe_city(city = "Amsterdam")
describe_city(city = "The Hague")
describe_city(city = "Paris")

'''8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians() , which prints the name of each magician in the list.'''

magicians = ["Hans Kazan", "Houdini", "Hans Klok"]


def show_magicians(list_):
    for item in list_:
        print(item)


print(show_magicians(magicians))

'''8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by add-
ing the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.'''


def make_great(list_):
    for index in range(list_.__len__()):
        list_[index] = "the Great " + str(list_[index])


magicians2 = magicians.copy()

make_great(magicians2)
show_magicians(magicians2)

'''8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the origi-
nal names and one list with the Great added to each magician’s name.'''

show_magicians(magicians)
show_magicians(magicians2)

'''8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that is being ordered. Call the function three times, using a different num-
ber of arguments each time.'''

def sandwich_maker(*args):
    items = ", ".join(*args)
    print(f"You ordered a sandwich with {items}.")


sandwich1 = ["salad", "cheese", "bacon", "tomato"]
sandwich2 = ["salmon", "fresh cheese"]
sandwich3 = ["humus", "salad", "aubergine", "courgette", "red pepper"]

sandwich_maker(sandwich1)
sandwich_maker(sandwich2)
sandwich_maker(sandwich3)


'''8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile() , using your first and last names
and three other key-value pairs that describe you.'''


def build_profile(first_name, last_name, **kwargs):
    print("First name: ", first_name)
    print("Last name: ", last_name)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


build_profile("Robert-Jan", "Lub", Nationality="Dutch", Hair="Blonde", Eyes="Blue")

'''8-14. Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.'''


def car_info(manufacturer, model_name, **kwargs):

    car_dict = dict()
    car_dict["manufacturer"] = manufacturer
    car_dict["model name"] = model_name

    for k, v in kwargs.items():
        car_dict[k] = v

    return car_dict


print(car_info("Ford", "Fietsa", color="grey", doors="3", year="2000"))

'''8-15. Printing Models: Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.

--> skipped

8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

--> skipped

8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.

--> applied during coding.
'''

