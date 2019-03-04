import datetime
import json

'''10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by read-
ing in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.'''

file = "ProjectDocuments/learningpython.txt"

for i in range(3):
    print(open(file).read())

with open(file, 'r') as fin:
    for lines in fin:
        print(lines)

with open(file,'r') as fin:
     my_text = fin.readlines()

cleaned_text = []

for text in my_text:
    cleaned_text.append(text.rstrip("\n"))
print(cleaned_text)


'''10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
message = "I really like dogs."
message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.'''

with open(file, 'r') as fin:
     my_text = fin.readlines()

cleaned_text = []

for text in my_text:
    cleaned_text.append(text.replace("python", "java").rstrip())

print(cleaned_text)

'''10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.'''
#
# name = input("What is your name, dear madam or sir?")
#
# with open("ProjectDocuments/guest.txt", "w") as fin:
#     fin.write(name)

'''10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.'''

flag = True
while flag:

    with open("ProjectDocuments/guest_book.txt", "a") as fin:
        name = input("What is your name, dear madam or sir? (type exit to exit)")
        if name.lower() == "exit":
            flag = False
        else:
            print(f"Greetings, {name}!")
            fin.write(f'The following person logged on: {name} at {datetime.datetime.now()}\n')


'''10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.'''

# flag = True
# while flag:
#
#     with open("ProjectDocuments/responses.txt", "a") as fin:
#         reason = input("Why do you like programming? (type exit to exit)")
#         if reason.lower() == "exit":
#             flag = False
#         else:
#             fin.write(f'Someone like programming because: {reason}\n')

'''10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a TypeError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.'''

# try:
#     num1 = int(input("Give the first number for the addition."))
#     num2 = int(input("Give the second number for the addition."))
#
# except ValueError:
#     print("You did not enter valid numbers. "
#           "To make the addition please make sure your data are integers or floats.")
#
# else:
#     print(float(num1) + float(num2))

'''10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.'''
# flag = True
# while flag:
#     try:
#         num1 = int(input("Give the first number for the addition."))
#         num2 = int(input("Give the second number for the addition."))
#
#     except ValueError:
#         print("You did not enter valid numbers. "
#               "To make the addition please make sure your data are integers or floats.")
#
#     else:
#         print(float(num1) + float(num2))
#         flag = False

'''10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.'''

# file1 = "ProjectDocuments/cats.txt"
# file2 = "ProjectDocuments/dogs.txt"
#
# documents = []
# documents.append(file1)
# documents.append(file2)
# documents.append("Not existing file")
#
# with open(file1, 'w') as cats:
#     cats.write("Nero\n")
#     cats.write("Chef\n")
#     cats.write("Lion\n")
#
# with open(file2, 'w') as dogs:
#     dogs.write("Rufus\n")
#     dogs.write("Max\n")
#     dogs.write("Nes\n")
#
#
# for doc in documents:
#     try:
#         my_pets = []
#         with open(doc, 'r') as pets:
#             my_pets = pets.readlines()
#
#     except FileNotFoundError:
#         print("This is not a valid file.")
#
#     else:
#         for pet in my_pets:
#             print(pet.rstrip())

'''10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
line = "Row, row, row your boat"
line.count('row')
2
line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.'''

# oz = "ProjectDocuments/The Marvellous Land of Oz.txt"
#
# with open(oz, 'r') as oz:
#     print(oz.read().lower().count("the"))


'''10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”'''

# user_num = []
#
# while True:
#     user_inp = input("Tel me your favorite number. I will keep it secret, I promise. "
#           "(Enter exit to exit.")
#     try:
#         user_num.append(int(user_inp))
#
#     except ValueError:
#         if user_inp.lower() == "exit":
#             break
#         print("That's no number! Don't try to fool me...")
#
#
#
# with open("ProjectDocuments/FavNums.txt", 'w') as favnum_file:
#     json.dump(user_num, favnum_file)
#
# with open("ProjectDocuments/FavNums.txt", 'r') as favnum_file:
#     loaded_nums = json.load(favnum_file)
#
# print(f'I know your favorite numbers. They are: {", ".join(str(num) for num in loaded_nums)}, and I will tell everyone. Muhahaha, you fool, '
#       f'you shouldn\'t have trusted me...')


'''10-13. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
Before printing a welcome back message in greet_user() , ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.'''

