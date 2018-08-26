##

# Dictionaries are unordered mappings for storing objectes. 
# Dictionaries use a key-value pairing system. This key-value pair allows users to quickly grab objects without needing to know an index location. 
# Dictionaries use curly braces and colons to signify the keys and their associated values. 
# 	{'key1':'value1','key2':'value2'}

# Dictionaries: 
# 	objects retrieved by key name
# 	Unordered and cannot be sorted

# Lists: 
# 	Objects retrieved by location.
# 	Ordered Sequences can be indexed and sliced.

my_dict = {'key1':'value1','key2':'value2'}
my_dict = ['key1']
# Returns 'value1'

prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5.80}
prices_lookup['apple']
# Returns 2.99

#Dictionaries can hold lists and even nest other dictionaries.
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
d['k2'] # Returns 'k2' list
d['k3']['insideKey'] # Returns 100



# Dictionary Methods

d = {'k1': 100, 'k2': 200, 'k3': 300}
d.keys() # Returns all keys
d.values() # Returns all values
d.items() # Returns all pairs