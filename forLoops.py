## 
# Many objects in Python are 'iterable'.
# the term iterable means you can iterate over the object.

# For example, you can iterate over every character in a string, iterate over every item in a list, iterate over every key in a dictionary.

# Syntax of a for loop

my_iterable = [1,2,3] # Statement
for item_name in my_iterable: # for every item in this list
	print(item_name) # print every item


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
	print(num)

# Returns 1 - 10 



for num in mylist: 
	print('hello')
# Returns 'hello' ten times, one for ever num in mylist



# Print only even numbers in mylist

for num in mylist:
	# Check for even
	if num % 2 == 0: # if there is no remainder when dividing by two, the number is even, so the num is printed. 
		print(num)
	else: # Print odd number with the following string
		print(f'Odd Number: {num}') # Using f-string to print the num at the end of the string

# Returns 
# Odd Number: 1
# 2
# Odd Number: 3
# 4
# etc.



# Get the sum of every number in mylist
list_sum = 0
for num in mylist: 
	list_sum = list_sum + num
print(list_sum)
# Returns 55 


# including the final 'print(list_sum)' into the for loop would create a new log for each step.
list_sum = 0
for num in mylist: 
	list_sum = list_sum + num
	print(list_sum)
# Returns 1, 3, 6, 10, 15, 21, etc.. 


# Looping through Strings
mystring = "Hello World"
for letter in mystring:
	print(letter)
# Returns h, e, l, l, o etc..

# You can also add string directly to for loop w/o a var. 
for letter in 'Hello World':
	print(letter)
# Returns the same as above


# If you don't intend to use var from for loop a simple _ can take the first var's place.
for _ in 'Hello World':
	print('Cool!')
# Returns 'Cool!' for every letter in the provided string 




# For loops and Tuples
tup = (1,2,3)
for item in tup:
	print(item)
# Returns 1, 2, 3



# Tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]
len(mylist) # Returns 4 since there are 4 tuple pairs

for item in mylist:
	print(item)
# Returns (1,2) (3,4) etc


# To Do Tuple unpacking
for (a,b) in mylist:
	print(a)
	print(b)
# Returns 1 2 3 4 5 6 etc

for a,b in mylist: # No Parentheses are necessary
	print(a)
# Returns 1 3 5 7



# Iterating through a dictionary

# By defualt, dictionaries iterate through key

d = {'k1':1,'k2':2,'k3':3}

for item in d:
	print(item)

# Returns k1 k2 k3


# To pull keys and values
for item in d.items():
	print(item)

# Returns ('k1', 1) ('k2', 2) ('k3', 3)


# Unpacking a Dictionary

for key,value in d.items():
	print(value)

# Returns 1 2 3







