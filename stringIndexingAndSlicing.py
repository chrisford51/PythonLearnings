##
# Indexing

# Establish Variable and String
mystring = "Hello World"
mystring # prints "Hello Wolrd"

# Using variable, follow with brackets containing the id of the character necessary to return
mystring[0] # Returns 'H' because that is the first character

mystring[8] # Returns 'r' since that is the 8th character

mystring[9] # Returns 'l' 

# Reverse Indexing
# Starting at the first letter, [0] or 'H', we can go backwards in the string to find the reverse index of a character. 

# Character:	H e l l o   W  o  r  l  d
# index:	<-	0			  -4 -3 -2 -1		<-

mystring[-4] # Returns 'o' because it is the 4 character from the end of the string. 

#Slicing

# set new String 
mystring = 'abcdefghijk'

# Starting at the 2nd index and printing the rest of the sequence 
mystring[2:] # would print 'cdefghijk'

# Starting at the begining of the string, but requesting all of the characters up to but not including a certain index.
mystring[:3] # would print 'abc'

#Starting at the 3rd index and requesting all of the character up to but not including the 6th index
mystring[3:6] # would print 'def'

mystring[1:3] # would print 'bc'


# Grab the whole string using the step function
mystring[::] # would print the whole string from beginning to end
# mystring[::] is the same thing as mystring[::1]
# Steps by default are 1 step at a time

mystring[::2] # would print the string with steps of 2, 'acegik'

mystring[::3] # would print the string with steps of 3, 'adgj'

# Start at index 2, stopping at but not including index 7 at a step of 2.
mystring[2:7:2] # would print 'ceg'


# Reverse a string using step size
mystring[::-1] # would print string backwards

##