##

# Immutability
# Strings cannot be updated or changed by indexing individual elements

name = "Sam"

# Wanting to change the first letter but strings are immutable so an error will occur. 
# 	name[0] = 'P'

# Slice 'am' off of original name variable and assign it to a new variable
last_letters = name[1:] # results in 'am'



# Concatenate last letters to new string of 'P'
name = 'P' + last_letters # Returns "Pam"

x = "Hello World"
x + " it is beautiful outside!" # Returns "Hello World it is beautiful outside!"

# set x equal to that concatenation so the x variable has now changed to the new complete string
x = x + " it is beautiful outside!"

# string multiplication
letter = 'z'
letter * 10 # returns 'zzzzzzzzzz'

# You are going to get errors if you try to concatenate numbers.
# '2' + '3' will not add, it will concatenate

# Methods
x = 'Hello World'
x.upper() # Prints string in uppercase
x.lower() # Prints string in lowercase
x.split() # Prints split string based on whitespace or letter thrown into function, ["Hello", "World"]




##