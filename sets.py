##

# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same object

myset = set()
myset # Returns set()

myset.add(1)
myset # Returns {1}

myset.add(2)
myset # Returns {1,2}

mylist = [1,1,1,1,1,2,2,2,4,3,3,3]
set(mylist)
# Returns only items that weren't repeated, {1,2,4,3}.

