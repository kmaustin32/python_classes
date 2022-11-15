
# Formatted strings. This will convert type too, so no need for str(age).
# Also, you can take a string, and add .format(name, age) with blank braces.
user_name = input("What is your name? >> ")
age = input("And your age? >> ")
print(f"Hello {user_name}!, you are {age}")

# Math Functions
print(round(3.23))
print(abs(-20))

# Divide and Round
print(7 // 3)

# Complex, a third type after Int and Float
# Bin will turn into a binary
print(bin(5))
# Turn that binary into a base 2 integer
print(int('0b101', 2))

# Variables in Python don't have a var, const, let designation
# Snake_case for normal variables, CAPS for constants 
# __ is called a dunder, aka a double under. These are keywords.
my_name = "Ezra"
PI = 3.14

# You can define multiple variables at once.
a,b,c = 1, 2, 3

# Expression is a piece of code that produces a value (right side)
# A statement is an entire line of code (whole thing)
user_age = 80 / PI
print(round(user_age, 2))

# Augmented assignment operator 
some_value = 5
some_value = some_value + 2

# or instead, we can use augmented assignment
some_value += 3

# Strings...
'This is a string, like it is in most languages...'
"This is also a string..."
'''
And this is
a long
string...
'''

# You can use + to concat. first_name + " " + last_name

# Type conversions...str, int, float, etc are ways to convert types. 
print(type(int(str(100))))

# Escape sequneces \ \t is tab, \n is new line
weather = "\t It\'s \"Kind of\" sunny, \n I hope you have a good day!"
print(weather)

#String index, seems much like an array. End is not inclusive. You can also do step over. So, 2 would grab every other. Defaults are beginning, end, and single, and [-1] will grab final. [::1] will reverse the string. This is the same as JS slicing and reversing, etx. 

selfish = 'me me me'
print(selfish[0:2:1])

# Strings are immutible 

# Functions. Rememeber that len(str) is the same as JS str.length()
# Methods take the .format()

quote = 'to be or not to be'
print(quote.upper())

# Should return 3, the index where this string starts
print(quote.find('be'))

# Should replace every occourance of be with me
print(quote.replace('be', 'me'))

# Remeber that strings are immutable, and thus when we run these methods, we are creating a new string. It's not saved to a variable, so it just goes away after the print, but it is a new string. 

# Booleans will be True or False
is_cool = True

# A small challenge. Find age from birth year
birth_year = input("When were you born? >> ")
age = abs(int(birth_year) - 2022)
print(age)

# Password check exercise

user_name = input("Please enter a user name >>  ")
password = input("Please input a password >> ")
pass_len = len(password)

print(f"Hi {user_name} your password {pass_len * '*'} is {pass_len} long.")

# Remember, setting one list to another will point to the same memory location. if you need to duplicate a list, set list2 = list1[:] to slice the list. So, a list is just basically a JS array. 

# What about a matrix? This is a multidemensional array. 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Again, much like in JS, accessing nested arrays will be like matrix[0][2] to grab the number 3 from the above matrix. 

basket = [1, 2, 3, 4, 5]
basket.append(100)
new_basket = basket
print(new_basket)

# .append(), .insert(), etc modify in place, does not create the copy of the list, so you need to make a new variable. .extend([]) takes another list, and adds the values in another list. 

# .pop() removes, as you may imagine. By default, removes the final item in the list. You can add the index of the element as an argument. .remove() will actually take a specific value and remove it. Pop will return the removed item.

new_basket.pop()

# .clear() will remove the list, as you might imagine. .index(x) will take a value and tell me where it is in the list. You can tell it where to start and stop looking as additional arguments, .index(x, 15, 30).

print(3 in basket) # should return true
print(basket.count(4)) # should return 1, as there is 1 instance of 4

# .sort() will sort a list, has no return value, so don't print it. sorted(arr) will produce a new array. .copy() will copy and return. .reverse() will do exactly what you think it will. Try sorting before reversing. 

# you can reverse a list with slice
basket[::-1]

# create a list. range(100) will go 0-99, because computers.
list(range(1,100))

# What about .join(). It creates a new string, so you need a new variable
join_sentence = ' '
new_sentence = join_sentence.join(['Hi', 'my', 'name', 'is', 'JOJO'])

# List unpacking. Assign variables from an established list. 
to_unpack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, c, *other, d = to_unpack

# What is None? It's an important keyword/data type. It's the absence of value, much like null in JS. Like, initiate a variable with no value. 

weapons = None

# Dictionaries. This is an Object, or a Hashtable. 

user_data = {
    'name': 'Keenan',
    'age': 30,
    'coding': True,
    'my_list': [1, 3, 5, 7, 9]
}

print(user_data['my_list'][2])

# You can check if a key exists with .get() and you can add a default value if it doesn't exist as well.

print(user_data.get('fav_food', 'shawarma'))

user2 = dict(name='JohnJohn')

print('age' in user_data.keys())
print(True in user_data.values())

# dict.items() will return tuples, which I don't know what those are. and, of course, .clear() will clean out the object. .pop(key) will remove that key/value pair and returns what was removed. .popitem() will remove last entered. .update will do that it sounds like. 

user_data.update({'age': 31})

# Tuple is like an immutible list. No sorting, reversing, etc. It may be accessed through an index. 
my_tuple = (1, 2, 3, 4, 5)

# Why do we need this? If you never need to change the list, it tells other programmers not the change the list. Slightly faster than a list. Like, lat, long will not change on a map. 

# SETS, let's gooooooo. These are unordered lists of unique objects. 

my_set = {1, 2, 3, 4, 5, 5, 3, 5}
print(my_set) # Should return {1, 2, 4}

# You can convert a list to a set with the set() function. 
# A set grabs by item name, not by index. 





