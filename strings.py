##
# Sequences of characters using single quotes or double quotes

'Hello'
"World"

# Strings are ordered sequences which means Indexing and Slicing can be used.

# Indexing assigns each character in the string an ID, starting with 0.

# Character: 	h e l l o
# Index: 		0 1 2 3 4  

# Reverse Index would allow one to grab the last few characters of the string without knowing how long the string is

# Character: 		h  e  l  l  o
# Reverse Index: 	0 -4 -3 -2 -1

# Slicing allows you to grab a subsection of multiple characters.
# Using the following syntax: 
#	[start:stop:step]

# Start is the index for the start of the slice
# Stop is the index you will go up to, but not include.
# Step is the size of the jump you make from start to stop.

"This is also a string"
# Whitespace also counts as a character for indexing.

"I'm going on a run" # If character is a single quote, the string cannot be wrapped in single quotes, it will have to be wrapped in double quotes.


# Print stings
print("Hello")

print('Hello World') # Prints on one line
print('Hello \n World') # Prints on separate lines including whitespace between \n and words



# Length function
len('Hello')
# Prints 5 because there are 5 characters.

len('I am')
# Prints 4 because it includes whitespace.

##