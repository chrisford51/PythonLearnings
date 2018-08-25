
# Rules for Variable names
# Names cannot start with a number
# There can be no spaces in the name, use '_' instead
# Can't use any of these symbols:
# : ' " , < > / ? | \ ( ) ! @ # $ % ^ & * ~ - +
# Per PEP8, variables are recommended to be lowercase

# Uses Dynamic Typing

# Assign
a = 5

# Reassign
a = 10

# Add 
a + a 

# Assign
a = 10

#	Take assigned variable, add it to itself and a new value is assigned to the variable.
#	20=10+10
	a = a + a 
a # would print 20


type(a)
	# would show that a is an int

a = 30.1
type(a)
	# would show that a is a float

# int = 4 cant work because int can't be used as a var since it is special character


my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate

my_taxes # would print 100 * 0.1 would is 10.0.

