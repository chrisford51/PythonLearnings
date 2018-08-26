##

# Lists are ordered sequences that can hold a variet of object types
# They use [] brackets and commas to separate objects in the list
#	[1,2,3,4,5]
# Lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them.

my_list = [1,2,3]
my_list = ['STRING', 100, 23.2]

len(my_list)
# Returns number if items in the list, 3 in this case.

mylist = ['one', 'two', 'three']
mylist[0]
# Returns 'one'
mylist[1:]
# Returns ['two','three']
another_list = ['four','five']

mylist + another_list
# Returns ['one', 'two', 'three', 'four','five']

new_list = mylist + another_list

new_list
# Returns ['one', 'two', 'three', 'four','five']



# Lists are mutable
new_list[0] = 'ONE ALL CAPS'
new_list
# Returns ['ONE ALL CAPS', 'two', 'three', 'four','five']

# Add item to the end of a list
new_list.append('six')
# Returns ['ONE ALL CAPS', 'two', 'three', 'four','five', 'six']

new_list.append('seven')
# Returns ['ONE ALL CAPS', 'two', 'three', 'four','five', 'six', 'seven']



# Remove an item from the end of a list
new_list.pop()
# Returns 'seven'
new_list 
# Returns ['ONE ALL CAPS', 'two', 'three', 'four','five', 'six']

popped_item = new_list.pop()
# Assigns popped item to variable.
popped_item
# Returns 'six'
new_list
# Returns ['ONE ALL CAPS', 'two', 'three', 'four','five']

# ID can be passed through pop method to remove a specific id.
new_list.pop(0)
# Returns 'ONE ALL CAPS'
new_list
# Returns ['two', 'three', 'four','five']




# Sort and Reverse Methods

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

new_list.sort() # Nothing is returned; Method is in-place
num_list.sort() # Nothing is returned; Method is in-place

new_list
# Returns ["a", "b", "c", "e", "x"]
num_list
# Returns [1, 3, 4, 8]

num_list.reverse()
num_list
# Returns [8, 4, 3, 1]
##