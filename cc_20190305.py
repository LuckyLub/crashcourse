'''11-1. City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country , such as Santiago, Chile . Store the function in a module called
city _functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.'''

def place(city, country, population=""):
    if population =="":
        return f"{city}, {country}"
    else:
        return f"{city}, {country} - population {population}"

'''11-2. Population: Modify your function so it requires a third parameter,
population . It should now return a single string of the form City, Country –
population xxx , such as Santiago, Chile – population 5000000 . Run
test_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run
test_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that veri-
fies you can call your function with the values 'santiago' , 'chile' , and
'population=5000000' . Run test_cities.py again, and make sure this new test
passes.'''

'''11-3. Employee: Write a class called Employee . The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee . Write two test methods, test_give_
default_raise() and test_give_custom_raise() . Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.'''

class Employee:

    def __init__(self,first_name, last_name, annual_salary):

        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def give_raise(self, bonus=5000):
        self.annual_salary = self.annual_salary + int(bonus)


if __name__ == '__main__':
    print(place("a","b",10))
    mark = Employee("Mark", "Moerman", 100000)
    mark.give_raise()
    print(type(mark.annual_salary))