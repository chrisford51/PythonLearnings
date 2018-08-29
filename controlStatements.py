## 
# To control the flow of logic we use some keywords:

if 
elif
else

# Control Flow syntax makes use of colons and indentation (whitespace)
# This indentation system is crucial to Python and is what sets it apart from other programming languages. 

# Syntax for an if/else statement

if some_condition:
	# execute some code
else:
	# do something else


if some_condition:
	# execute some code
elif some_other_condition: 
	# do something different
else:
	# do something else

# Examples

if True: 
	print('ITS TRUE!')
	# Returns 'ITS TRUE!'



hungry = True
if hungry:
	print('feed me')
#returns 'feed me'



hungry = False
if hungry:
	print('feed me')
else:
	print('Im not hungry')
# Returns 'im not hungry'




loc = 'bank'

if loc == 'auto shop':
	print('cars are cool')
elif loc == 'bank'
	print('money is cool')
elif loc == 'store'
	print('welcome to the store')
else:
	print('i do not know much')



name = 'Sammy'

if name == 'Frankie':
	print('Hello Frankie')
elif name == 'Sammy'
	print('Hello Sammy')
else: 
	print("What is your name?")


