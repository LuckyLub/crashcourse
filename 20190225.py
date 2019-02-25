'''4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.'''
''''''
menu = ("Pasta Bolognaise", "Nasi Goreng", "Bami Goring", "Red cury", "Pizza")

for food in menu:
    print(food)

menu = ("apple", "banana", "citron", "Red cury", "Pizza")

for food in menu:
    print(food)


'''
4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/
dev/peps/pep-0008/. You won’t use much of it now, but it might be interesting
to skim through it.

--> Skipped

4-15. Code Review: Choose three of the programs you’ve written in this chapter
and modify each one to comply with PEP 8:
• Use four spaces for each indentation level. Set your text editor to insert
four spaces every time you press tab , if you haven’t already done so (see
Appendix B for instructions on how to do this).
• Use less than 80 characters on each line, and set your editor to show a
vertical guideline at the 80th character position.
• Don’t use blank lines excessively in your program files.

--> Skipped

5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False .
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False .
'''

for food in menu:
    if food == "Red cury":
        print("Hmmmm, jammie!")
    if food == "banana" or food == "Red cury": #when not using elif it is a new comparison.
        print("That's so exotic!")
    else:
        print("Boooooh!!")

'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

text1 = "This is something."
text2 = "THIS is something else."
text3 = "this is something else."

print(f'text1 equals text 2: {text1 == text2}')
print(f'text1 equals text 3: {text1 == text3}')
print(f'text2 equals text 3: {text2 == text3}')
print(f'text1.lower equals text 2.lower: {text1.lower() == text2.lower()}')
print(f'text1.lower equals text 3.lower: {text1.lower() == text3.lower()}')
print(f'text2.lower equals text 3.lower: {text2.lower() == text3.lower()}')
print(f'2 < 1: {2 < 1}')
print(f'0 < 1: {0 < 1}')
print(f'1 == 1: {1 == 1}')
print(f'0 <= 1: {0 <= 1}')
print(f'0 == 0 and 1 == 1: {0 == 0 and 1 == 1}')
print(f'0 == 2 and 1 == 1: {0 == 2 and 1 == 1}')
print(f'0 == 2 or 1 == 1: {0 == 2 or 1 == 1}')
print(f'apple in menu: {"apple" in menu}')
print(f'banana not in menu: {"banana" not in menu}')

'''5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red' .
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if - else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
5-5. Alien Colors #3: Turn your if - else chain from Exercise 5-4 into an if - elif -
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.'''

alien_colors = ["Green", "Yellow", "Red"]
import random
alien_color = random.choice(alien_colors)

if alien_color == "Green":
    print("You just earned 5 points for shooting the alien.")
elif alien_color == "Yellow":
    print("You just earned 10 points")
else:
    print("You just earned 15 points")



'''
5-6. Stages of Life: Write an if - elif - else chain that determines a person’s
stage of life. Set a value for the variable age , and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.'''

def stages_of_life(age):
    if age < 2:
        print(f'This person is a baby.')
    elif age <= 2 and age < 4:
        print(f'This person is a toddler.')
    elif age <= 2 and age < 4:
        print(f'This person is a kid.')
    elif age <= 13 and age < 20:
        print(f'This person is a teenager.')
    elif age <= 20 and age < 65:
        print(f'This person is an adult.')
    else:
        print(f'This person is an elder.')

ages = [0, 10, 20, 30, 40, 50, 60, 70, 80]

for age in ages:
    stages_of_life(age)


'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits .
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!'''


favorite_fruits = ["apple", "banana", "citron", "dragon fruit"]

for fruit in favorite_fruits:
    if fruit == "apple":
        print(f"I adore {fruit}")
    elif fruit == "banana":
        print(f"I bake {fruit}")
    elif fruit == "citron":
        print(f"I cant go without {fruit}")
    elif fruit == "dragon fruit":
        print(f"I dig {fruit}")
    else:
        print("My favorite fruit is not in here...")
'''
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin' . Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin' , print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
ging in again.
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.'''


usernames = ["admin", "Martin", "Caden", "Melissa", "Casey", "Ben", "Daniel", "Michael", "Ming"]

def using_users(usernames):
    if usernames.__len__() != 0:
        for name in usernames:
            if name == "admin":
                print("Hello admin, would you like to see a status report?")
            else:
                print(f'Hi there, {name}! Thank you for log-ging in again.')
    else:
        print("We need to find some users.")

using_users(usernames)
using_users([])

'''5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users .
• Make another list of five usernames called new_users . Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•
Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.'''

existing_users =["admin", "Martin", "Caden", "Melissa", "Casey"]
new_users = ["Melissa", "Casey", "Ben", "Daniel", "Michael", "Ming"]

for new_user in new_users:
    check = 0
    for existing_user in existing_users:
        if new_user == existing_user:
            check = 1
    if check == 1:
        print("This username is already used. You have to pick a new one.")
    else:
        print(("This username is available"))

'''5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if - elif - else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th" , and each result should be on a separate line.'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f'{number}th')

'''5-12. Styling if statements: Review the programs you wrote in this chapter, and
make sure you styled your conditional tests appropriately.
5-13. Your Ideas: At this point, you’re a more capable programmer than you
were when you started this book. Now that you have a better sense of how
real-world situations are modeled in programs, you might be thinking of some
problems you could solve with your own programs. Record any new ideas you
have about problems you might want to solve as your programming skills con-
tinue to improve. Consider games you might want to write, data sets you might
want to explore, and web applications you’d like to create.'''
