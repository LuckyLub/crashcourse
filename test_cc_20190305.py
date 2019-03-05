'''11-1. City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country , such as Santiago, Chile . Store the function in a module called
city _functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.

11-2. Population: Modify your function so it requires a third parameter,
population . It should now return a single string of the form City, Country –
population xxx , such as Santiago, Chile – population 5000000 . Run
test_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run
test_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that veri-
fies you can call your function with the values 'santiago' , 'chile' , and
'population=5000000' . Run test_cities.py again, and make sure this new test
passes.
'''

import unittest
import cc_20190305

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.employee1 = cc_20190305.Employee("Mark", "Moerman", "100000")

    def test_if_2_strings_are_joined_together(self):
        self.assertEqual(cc_20190305.place("Santiago","Chile"),"Santiago, Chile")

    def test_if_population_can_be_added_to_description(self):
        self.assertEqual(cc_20190305.place("Santiago", "Chile", 5000000), "Santiago, Chile - population 5000000")

    def test_if_raise_method_adds_5000_to_annual_salary(self):
        expected_outcome = self.employee1.annual_salary + 5000
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, expected_outcome)

    def test_if_raise_method_adds_user_defined_raise_to_annual_salary(self):
        user_defined_raise = 30000
        expected_outcome = self.employee1.annual_salary + user_defined_raise
        self.employee1.give_raise(user_defined_raise)
        self.assertEqual(self.employee1.annual_salary, expected_outcome)


