##

# Often you will want to inject a variable into your string for printing. For example: 
#	my_name = "Chris"
#	print("Hello " + my_name)
# There are multiple ways to format strings for printing variables in them.
# This is know as String Interpolation

#Methods:
#	.format()
#	f-strings


# .format()
#
# 'String here {} then also {}'.format('something1','something2')

print('This is a string {}'.format('INSERTED'))
# Returns 'This is a string INSERTED'

print('The {} {} {}'.format('fox', 'brown', 'quick'))
# Returns 'The fox brown quick'

# Using IDs of entered  in the .format method can be used in the curly braces to arrange inserts.
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# Returns 'The quick brown fox'

# The keys in .format can be assigned specific identifier properties from within the method.  
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
# Returns 'The quick brown fox'

# Float formatting
# Float formatting follows "{value:width.precision f}"

result = 100/777
result # Returns 0.1287001287001287

print("The result was {r}".format(r=result))
# Returns 0.1287001287001287

print("The result was {r:1.3f}".format(r=result))
# Returns 0.129


# f-string
# Formatted string literals

name = "Jose"
print('Hello, his name is {}'.format(name))
# Returns 'Hello, his name is Jose

# f-string example
print(f'Hello, his name is {name}')
# Returns 'Hello, his name is Jose

name = "Sam"
age = 3

print(f'{name} is {age} years old.')
# Returns Sam is 3 years old.

##