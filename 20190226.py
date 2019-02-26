'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name , last_name , age , and city . Print each
piece of information stored in your dictionary.'''

judith_dict = {"name" : "Judith", "last name": "Kamp", "age" : "27", "city" : "The Hague"}

print(judith_dict.items())
print(judith_dict.keys())
print(judith_dict.values())

for key, value in judith_dict.items():
    print(key, value)


'''6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.'''

favorite_numbers = {"Robert" : 23, "Daniel": 17, "Blake" : 420, "Ming" : 33, "Casey" : 167}

for key, value in favorite_numbers.items():
    print(f"{key}'s favorite number is {value}.")

'''6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character ( \ n ) to insert a blank line between each word-meaning
pair in your output.'''

python_glossary = {"range": "creates a list of numbers from a start point to an end point, with a certain step.",
                   "loop": "Iterating over data, can be done with for or while",
                   "dictionary": "A class which stores data by keys. A key needs to be unique and immutable, the value "
                                 "does not.",
                   "list": "Mutable and iterable class. Think of it as a book-shelf.",
                   "key": "An immutable class used within a dictionary to look up a value"}

for key, value in python_glossary.items():
    print(key, "|", value)

'''6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
-->  already done

6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
'''

rivers = {"Nile": "Egypt",
          "Rhine": "Netherlands",
          "Maas": "Belgium",
          "of Babylon": "Boney M",
          "Loboc": "Philippines"
          }

for key, value in rivers.items():
    print(f"The river {key} runs through {value}.")

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

'''6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.'''


people = ["John", "Joe", "Jack", "George", "Daniel", "Ming"]

for person in people:
    if person in favorite_numbers.keys():
        print(f"Thanks {person} for takig the poll!")
    else:
        print(f"Hello {person}, can you please fill in the poll?")

'''6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people . Loop through your list of people. As you
loop through the list, print everything you know about each person.'''

robert_dict = {"name" : "Robert-Jan", "last name": "Lub", "age" : "28", "city" : "The Hague"}
edith_dict =  {"name" : "Edith", "last name": "van Rees", "age" : "60", "city" : "Overijse"}

people = [robert_dict, judith_dict, edith_dict]

for person in people:
    for key, value in person.items():
        print(key,"|",value)

'''6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets . Next, loop through your list
and as you do print everything you know about each pet.'''

Doug = {"kind": "Dog",
        "owner": "Daniel"}
Ben = {"kind": "Bunny",
       "owner": "Bert"}
Catherine = {"kind": "cat",
             "owner": "Carl"}
Phill = {"kind": "Fish",
         "owner": "Freddy"}
Paul = {"kind": "Pony",
        "owner": "Patrick"}

pets = [Doug, Ben, Catherine, Phill, Paul]

for pet in pets:
    for key, value in pet.items():
        print(key,"|",value)

'''6-9. Favorite Places: Make a dictionary called favorite_places . Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.'''

favorite_places = {"John" : "Jeruzalem",
                   "Frederick" : "France",
                   "Paul" : "Portugal"
                   }

for key, value in favorite_places.items():
    print(f"{key}'s favorite place is {value}.")

'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.'''

favorite_numbers = {"Robert": 23, "Daniel": 17, "Blake": 420, "Ming": 33, "Casey": 167}

import random

for key, value in favorite_numbers.items():
    favorite_numbers[key] = [value, random.randint(0,100000)]

for key, value in favorite_numbers.items():
    number_str = str()
    for number in value:
        number_str += " " + str(number)
    print(f"{key}'s favorite numbers are{number_str}")

'''6-11. Cities: Make a dictionary called cities . Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country , population , and fact . Print the name of each city and all of the infor-
mation you have stored about it.'''

cities = {"Amsterdam": {"information": "I used to live here for 9 months",
                        "country": "Netherlands",
                        "population": 821752,
                        "fact": "Capital of the Netherlands."},
          "The Hague": {"information": "Place where I live.",
                        "country": "Netherlands",
                        "population": 514861,
                        "fact": "Political centre of the Netherlands."},
          "Rotterdam": {"information": "Place where I work.",
                        "country": "Netherlands",
                        "population": 623652,
                        "fact": "Biggest harbor from the Netherlands."}}

for key1, value1 in cities.items():
    for key2, value2 in value1.items():
        print(f'{key1} | {key2} | {value2}')

'''6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program or improving the formatting of the output.

--> skipped.'''


'''7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”'''

#car = input("What kind of car would you like?")
#print(f'Let me see if I can find you a {car}.')

'''7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message say-
ing they’ll have to wait for a table. Otherwise, report that their table is ready.'''

#customers = int(input("How many people are there in your dinner group?"))
#if customers > 8:
#    print("I'm sorry, but you will have to wait for a table.")
#else:
#    print("The table is ready. Please follow me.")

'''7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.'''

# number = int(input("Give me a number."))
#
# if number % 10 == 0:
#     print("This number is a multiple of 10.")
# else:
#     print("This number is not a multiple of 10.")

'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''

# toppings = []
# status = "go"
# while status == "go":
#     answer = input("What kind of topping would you like? If you don't want more toppings, type 'q'.")
#     if answer.lower() == "q":
#         status = "stop"
#     else:
#         toppings.append(answer)
#
# print(f'You are getting a pizza topped with: {toppings}')

'''7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''

# age = int(input("What's the age of the who wants to come in the movie?"))
#
# if age < 3:
#     print("This person can come in for free.")
# elif age >= 3 and age < 12:
#     print("The price for this person is $10.")
# else:
#     print("The price for this person is $15.")

'''7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
or close the window displaying the output.)

--> skipped

7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches . Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
in finished_sandwiches .'''

sandwich_orders = ["BLT", "pastrami", "Chilli Chicken", "pastrami", "Cheese", "pastrami"]
finished_sandwiches = []

print("Bad news! The deli run out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    print(f"I made your sandwich {sandwich_orders[0]}.")
    finished_sandwiches.append(sandwich_orders[0])
    del sandwich_orders[0]


print("We made the following sandwiches:", ', '.join(str(i) for i in finished_sandwiches))

'''7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.'''

destinations = {}

while True:
    dream_vacation = input("What would be your dream destination? Type 'exit' to exit poll.")
    if dream_vacation.lower() == "exit":
        for k, v in destinations.items():
            print(f"There are {v} people, that want to go to {k}.")
        break
    if dream_vacation.capitalize() in destinations.keys():
        destinations[dream_vacation.capitalize()] += 1
    else:
        destinations[dream_vacation.capitalize()] = 1


