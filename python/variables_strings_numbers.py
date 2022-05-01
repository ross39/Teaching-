message = "Hello from the message variable"
print(message)

# name error 
# Uncomment to see error 
# print(mesage)

# Both of these are valid strings
my_string = "This is a double-quoted string."
my_string_two = 'This is a single-quoted string.'

quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"
print(my_string)
print(my_string_two)
print(quote)

first_name = 'eric'

print(first_name)
print(first_name.title())
print(first_name.upper())
print(first_name.lower())

# These share similar variable so commented to avoid error 
# first_name = 'ada'
# last_name = 'lovelace'

# full_name = first_name + ' ' + last_name

# print(full_name.title())

# Let's discuss whitespaces!
# The term "whitespace" refers to characters that the computer is aware of
# but are invisible to readers. The most common whitespace characters are spaces, tabs, and newlines.

print("Hello everyone!")
print("\tHello everyone!")
print("Hello \teveryone!")
print("Hello everyone!")
print("\nHello everyone!")
print("Hello \neveryone!")
print("\n\n\nHello everyone!")


# Getting rid of whitespaces!
# Many times you will allow users to enter text into a box, and then you will read that text and use it. It is really easy for people 
# to include extra whitespace at the beginning or end of their text. Whitespace includes spaces, tabs,and newlines.
# Therefore we might wish to 'sanitize' this user input before we do anything with it to avoid weird errors occuring
# Uncomment to see whitspace stripping in action! 

# name = ' eric '

# print('-' + name.lstrip() + '-')
# print('-' + name.rstrip() + '-')
# print('-' + name.strip() + '-')

# Lets talk integers! 
# An integer is just a whole number. So -9, 10, 88, 90 are all integers while 9.87, 76.54, 777.34 are not(they're called floating point numbers or floats)

print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)


# Lets talk floats! 
print(0.1+0.1)

# However, sometimes you will get an answer with an unexpectly long decimal part:
print(0.1+0.2)

# This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to 
# working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to 
# represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in 
# powers of two, and we see that in the answer to 0.1+0.2.

# Python tries to hide this kind of stuff when possible. Don't worry about it much for now; just don't be surprised by it, and know that we will learn to clean up our results a little later on
# You can also get the same kind of result with other operationsself.

print(3*0.1)
