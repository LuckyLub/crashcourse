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
and then uses each function introduced in this chapter at least once.'''
