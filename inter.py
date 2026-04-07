#lists: 
#list is a collection which is ordered and changeable.
#  Allows duplicate members.
#list is created using square brackets.
#list can contain different data types.
my_list = [1, "Hello", 3.14, True, [1, 2, 3]]
print(my_list)

# Accessing list items
print("first item:", my_list[0])
print("second item:", my_list[1])
print("last item:", my_list[-1])

# Modifying list items
my_list[1] = "World"
print("Modified list:", my_list)

# Adding items to a list
my_list.append("kiki")
print("List after appending:", my_list)

#removing items from a list
my_list.remove(3.14)
print("List after removing 3.14:", my_list)

my_list.pop(2)
print("List after popping index 2:", my_list)

my_list.clear()
print("List after clearing:", my_list)

my_list = [1, "Hello", 3.14, True, [1, 2, 3]]

my_list.count(1)
print("Count of 1 in the list:", my_list.count(1))

my_list.reverse()
print("Reversed list:", my_list)

my_list = [3, 1, 4, 2]
my_list.sort()
print("Sorted list:", my_list)

# using slices
numbers = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
print("Subset of numbers from index 2 to 8:", numbers[3:8])
print("Subset of numbers from index 0 to 4:", numbers[:5])
print("Subset of numbers from index 5 to the end:", numbers[5:])
print("Subset of numbers with a step of 3:", numbers[::3])
print("Subset of numbers with a step of 2 in reverse order:", numbers[::-2])
print("Subset of numbers from index 1 to 7 with a step of 2:", numbers[1:8:2])
print("Subset of numbers from index 7 to 1 with a step of -2:", numbers[7:0:-2])
print("Subset of numbers from index 0 to 9 with a step of 1:", numbers[0:9:1])