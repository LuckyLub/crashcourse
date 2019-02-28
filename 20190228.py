'''9-1. Restaurant: Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def desribe_restaurant(self):
        print(f"\nThis restaurant is called: {self.name}\n"
              f"They serve food of the following type: {self.cuisine_type}\n"
              f"They served a total of {self.number_served}\n")

    def open_restaurant(self):
        print(f"{self.name} is open for business.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_numbers_served(self, number):
        self.number_served += number


mama = Restaurant("Mama mia", "Italian")
vanya = Restaurant("Vanya Vodka", "Russian")
bistro = Restaurant("Bonjour", "French cuisine")

restaurants_list = [mama, vanya, bistro]


for restaurant in restaurants_list:
    restaurant.desribe_restaurant()
    restaurant.open_restaurant()


'''9-3. Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.'''


class Users:

    def __init__(self, first_name, last_name, nationality = None, length = None, date_of_birth = None):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.length = length
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def describe_user(self):
        print(f"We have the following information of {self.first_name}:\n\n"
              f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}\n"
              f"Nationality: {self.nationality}\n"
              f"Date of birth: {self.date_of_birth}\n"
              f"Length: {self.length}\n")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome back again.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


robert = Users("Robert-Jan", "Lub","Dutch", "182", "23-02-1991")
daniel = Users("Daniel", None, "French")
michael = Users("Michael", None, "Aussie")
ben = Users("Ben", None, "Canadian")
casey = Users("Casey", "King", "American")

user_list = [robert, daniel, michael, ben, casey]

for user in user_list:
    user.greet_user()
    user.describe_user()

'''9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.'''


for restaurant in restaurants_list:
    restaurant.open_restaurant()
    restaurant.set_number_served(100)
    restaurant.increment_numbers_served(167)
    restaurant.desribe_restaurant()

'''9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0.'''

for user in user_list:
    for i in range(10):
        user.increment_login_attempts()
        print(user.first_name, user.login_attempts)

    user.reset_login_attempts()
    print("Reset", user.first_name, user.login_attempts)

'''9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand , and call this method.'''

class IceCreamStand(Restaurant):

    def __init__(self,name, cuisine_type, flavors =[]):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def ice_cream_flavors(self):
        print(f"The flavors you can choose from are: {', '.join(self.flavors)}.")


flavors = ["strawberry", "banana", "melon", "vanilla", "chocolate"]

gelato = IceCreamStand("Jelly Gelato", "Ice cream", flavors)

gelato.ice_cream_flavors()

'''9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.'''


class Admin(Users):

    def __init__(self, first_name, last_name, privileges, nationality=None, length=None, date_of_birth=None):
        super().__init__(first_name, last_name, nationality, length, date_of_birth)
        self.privileges = Privileges(privileges)

    # def show_privileges(self):
    #     print(f"This person has the following privileges:")
    #     for privilege in self.privileges:
    #         print("\n", privilege)


# list_privileges = ["can add post", "can delete post", "can ban user", "can ride pony"]
# martin = Admin("Martin", "Breuss", list_privileges, "Austria", 180, "01-01-1988")
#
# martin = Admin("a","b",list_privileges)
#
# martin.show_privileges()

'''9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges , that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.'''


class Privileges:

    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"This person has the following privileges:")
        for privilege in self.privileges:
            print("\n", privilege)


list_privileges = ["can add post", "can delete post", "can ban user", "can ride pony"]
martin = Admin("Martin", "Breuss", list_privileges, "Austria", 180, "01-01-1988")

martin = Admin("a","b",list_privileges)

martin.privileges.show_privileges()

'''9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery() . This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.'''

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
            self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
            print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.1
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def upgrade_battery(self):
        self.battery.battery_size = 85

mycar = ElectricCar("Ford", "Fiesta", 2000)

print("capacity battery of mycar", mycar.battery.battery_size)

mycar.upgrade_battery()

print("capacity battery of mycar",mycar.battery.battery_size)


'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod-
ule. Make a separate file that imports Restaurant . Make a Restaurant instance,
and call one of Restaurant ’s methods to show that the import statement is work-
ing properly.

---> SKIPPED

9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User , Privileges , and Admin in one module. Create a sepa-
rate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.

---> SKIPPED

9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.


---> SKIPPED'''

'''9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.'''

from collections import OrderedDict

python_glossary = OrderedDict()

python_glossary["range"] = "creates a list of numbers from a start point to an end point, with a certain step."
python_glossary["loop"] = "Iterating over data, can be done with for or while"
python_glossary["dictionary"] = "A class which stores data by keys. A key needs to be unique and immutable, the value "\
                                "does not."
python_glossary["list"] = "Mutable and iterable class. Think of it as a book-shelf."
python_glossary["key"] = "An immutable class used within a dictionary to look up a value"


for key, value in python_glossary.items():
    print(key, "|", value)


'''9-14. Dice: The module random contains functions that generate random num-
bers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides , which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''
import random


class Die:

    def __init__(self,sides = 6):
        self.sides = 6

    def roll_die(self):
        return random.randint(0, self.sides)


die1 = Die()
die2 = Die(10)

die1outcomes = []
for i in range(10):
    die1.roll_die()
    die1outcomes.append(die1.roll_die())

die2outcomes = []
for i in range(20):
    die2.roll_die()
    die2outcomes.append(die2.roll_die())

print(die1outcomes)
print(die2outcomes)


'''9-15. Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
http://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, or explore the documentation of
the collections and random modules.

'''