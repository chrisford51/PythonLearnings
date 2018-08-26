##
# Tuples are very similar to lists except they have Immutability.
# Once an element is inside a tuple, it can not be reassigned. 
# Tuples use parenthesis (1,2,3)

t = (1,2,3)
mylist = [1,2,3]

# can use length operator
len(t) # Returns 3


# Can combine int and str
t = ('one', 2)

# Can use indexing and splicing
t[0] # Returns 'one'

# index method and count method
t = ('a', 'a', 'b')

# Count Method
t.count('a')
# Returns 2 because 'a' appears twice.

# Index Method
t.index('a')
# Returns 0 because 'a' first appears in the 0 index.
t.index('b')
# Returns 2 because 'b' first appears in the 2 index.



#Immuatability
mylist[0] = 'NEW'
mylist # Returns ['NEW', 2, 3]

# t[0] = 'NEW' Returns an error

