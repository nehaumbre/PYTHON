#Sets
# unordered collection of unique items

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_set = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(my_set)
print(type(my_set))

# print(my_set[0])  error: 'set' object is not subscriptable
# sets do not support indexing
# we cant access elements of a set by index because sets are unordered collections of unique items.
# we can only access elements of a set by iterating over it

#duplicate values are not allowed in sets
my_set = {1, 2, 3, 4, 5, 5, 5, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# add elements to a set
my_set.add(6)
print(my_set) 

# add multiple elements to a set
my_set.update([7,8,9,10])
print(my_set)

# delete elements from a set
my_set.remove(10)
print(my_set)
my_set.discard(9)
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

#iterate over a set
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
