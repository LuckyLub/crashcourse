'''Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises to keep
them organized.
3-1. Names: Store the names of a few of your friends in a list called names . Print
each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
person’s name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.” '''

names = ["Wim", "Alexander", "Robbert-Jan", "Wouter", "Jurre", "Victor", "Peter", "Jeroen", "Sander", "Douwe", "Melvin",
         "Stefan", "Willem"]

for name in names:
    print(name)

for name in names:
    print(f'Hello, {name}! How are you today?')

cars = ["Ferrari", "Lamborghini", "BMW", "Mercedes", "Audi"]

for car in cars:
    print(f"I would like to own a {car}.")

'''The following exercises are a bit more complex than those in Chapter 2, but
they give you an opportunity to use lists in all of the ways described.

3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.'''


for name in names:
    print(f'Hello, {name}! Want to come to my dinner?')

'''

3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.'''


print(f'Too bad, but {names[0]} and {names [1]} can\'t make it.')
del names[0]
del names[0]

names.append('Frank')
names.append('Christian')

for name in names:
    print(f'Hello, {name}! Want to come to my dinner?')


'''

3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''
for name in names:
    print(f'Hello, {name}! I found a bigger table, care to invite anyone else?')

names.insert(0, "Jean-Paul")
names.insert(5, 'Rutger')
names.append('Ruben')

for name in names:
    print(f'Hello, {name}! Want to come to my dinner?')

'''
3-7. Shrinking Guest List: 
You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program. '''

for name in names:
    print(f'Hello, {name}! I\'ve got some bad news. I made a mistake. The table only has room fo2 people?')

while names.__len__() > 2:
    names.pop(0)

for name in names:
    print(f'Good news, {name}! You are still invited?')

del names[0]
del names[0]

if names.__len__()==0:
    print("The list is empty now.")

'''3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without chang-
ing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.'''

places_to_visit = ["Australia", "New Zealand", "Kazachstan", "Iran", "Hawaii"]

print(places_to_visit)

print(sorted(places_to_visit))

print(places_to_visit)

places_to_visit.reverse()

print(places_to_visit)

places_to_visit.reverse()

print(places_to_visit)

places_to_visit.sort()

print(places_to_visit)

places_to_visit.sort(reverse=True)

print(places_to_visit)

'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.'''

names = ["Wim", "Alexander", "Robbert-Jan", "Wouter", "Jurre", "Victor", "Peter", "Jeroen", "Sander", "Douwe", "Melvin",
         "Stefan", "Willem"]

print("Length: ",names.__len__())

'''
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.

--> Skipped this one.


3-11. Intentional Error: If you haven’t received an index error in one of your
programs yet, try to make one happen. Change an index in one of your pro-
grams to produce an index error. Make sure you correct the error before clos-
ing the program.


print(places_to_visit[100])

4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!

'''
pizzas = ["Hawaii", "Quatro Fromagi", "Tuna"]

for pizza in pizzas:
    print(f'One of my favorite pizza\'s is {pizza}.')

print("You know I really like pizza\'s in general...")

'''

4-2. Animals: Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!

'''

cats = ["kitten", 'cheetah', "lion"]
for cat in cats:
    print(cat)

for cat in cats:
    print(f"A {cat} makes a great pet.")

print("They all are cats and cats make great pets!")

'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.'''

for i in range(20):
    print(i+1)


'''
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl -C or by closing the output window.)

for i in range(1000000):
    print(i+1)

4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.'''

numbers = []

for i in range(1000000):
    numbers.append(i+1)

print(min(numbers),max(numbers))
print(sum(numbers))

'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.'''

for i in range(1,20,2):
    print(i)



'''
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.'''

for i in range(1,11):
    print(i*3)

'''
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.'''

for i in range(10):
    print(i**3)

'''
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.'''

cubes = [i**3 for i in range(10)]
print(cubes)

'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list. '''


print("The first items in this list are: ", cubes[:3])
print("The middle items in this list are: ", cubes[3:6])
print("The last items in this list are: ", cubes[7:])

'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas .
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas .
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.'''

friends_pizzas = pizzas.copy()
friends_pizzas.append("salami")

print(pizzas == friends_pizzas)


print(f'My favorite pizza\'s are: ')
for i in pizzas:
    print(i)

print(f'My friends favorite pizza\'s are: ')
for i in friends_pizzas:
    print(i)


'''
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

--> Skipped
'''

