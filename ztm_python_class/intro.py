
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




