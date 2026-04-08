# #lists: 
# #list is a collection which is ordered and changeable.
# #  Allows duplicate members.
# #list is created using square brackets.
# #list can contain different data types.
# my_list = [1, "Hello", 3.14, True, [1, 2, 3]]
# print(my_list)

# # Accessing list items
# print("first item:", my_list[0])
# print("second item:", my_list[1])
# print("last item:", my_list[-1])

# # Modifying list items
# my_list[1] = "World"
# print("Modified list:", my_list)

# # Adding items to a list
# my_list.append("kiki")
# print("List after appending:", my_list)

# #removing items from a list
# my_list.remove(3.14)
# print("List after removing 3.14:", my_list)

# my_list.pop(2)
# print("List after popping index 2:", my_list)

# my_list.clear()
# print("List after clearing:", my_list)

# my_list = [1, "Hello", 3.14, True, [1, 2, 3]]

# my_list.count(1)
# print("Count of 1 in the list:", my_list.count(1))

# my_list.reverse()
# print("Reversed list:", my_list)

# my_list = [3, 1, 4, 2]
# my_list.sort()
# print("Sorted list:", my_list)

# # using slices
# numbers = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
# print("Subset of numbers from index 2 to 8:", numbers[3:8])
# print("Subset of numbers from index 0 to 4:", numbers[:5])
# print("Subset of numbers from index 5 to the end:", numbers[5:])
# print("Subset of numbers with a step of 3:", numbers[::3])
# print("Subset of numbers with a step of 2 in reverse order:", numbers[::-2])
# print("Subset of numbers from index 1 to 7 with a step of 2:", numbers[1:8:2])
# print("Subset of numbers from index 7 to 1 with a step of -2:", numbers[7:0:-2])
# print("Subset of numbers from index 0 to 9 with a step of 1:", numbers[0:9:1])

# 1D , 2D and 3D lists abd multidimensional lists

# list_1d = [1, 2, 3, 4, 5]
# print("1D list:", list_1d)

# list_2d =[[1,2,3],[3,4,5],[6,6,7]]
# print("2D list:", list_2d)

# list_3d = [[[1,2,3],[3,4,5],[6,6,6]],[[1,2,3],[3,4,5],[6,6,7]]]
# print("3D list:", list_3d)

# print(list_2d[2][2])
# print(list_3d[0][0][2])
# print(list_3d[1][1][2])
# print(list_3d[1][2][0])

#list built-in methods
# #append: appends an item to the end of the list. 
# # This method modifies the original list and does not return a new list.
# animeList = ["Naruto", "One Piece", "Attack on Titan"]
# animeList.append("Demon Slayer")
# print("Anime list after appending:", animeList)

# #extend: extends the list by appending all the items from another iterable (e.g., another list).
# # This method modifies the original list and does not return a new list.
# moreAnime = ["My Hero Academia", "Jujutsu Kaisen"]
# animeList.extend(moreAnime)
# print("Anime list after extending:", animeList)

# #insert: inserts an item at a specified index in the list.
# # This method modifies the original list and does not return a new list.
# animeList.insert(4, "Witch Hat Atelier")
# print("Anime list after inserting:", animeList)

# #remove: removes the first occurrence of a specified item from the list.
# # This method modifies the original list and does not return a new list.
# animeList.remove("Attack on Titan")
# print("Anime list after removing 'Attack on Titan':", animeList)

# #pop: removes and returns the item at a specified index in the list. If no index is specified, it removes and returns the last item in the list.
# # This method modifies the original list and returns the removed item.
# pop_anime = animeList.pop()
# print("Anime list after popping the last item:", animeList)
# print("Popped anime:", pop_anime)

# #pop at index 2
# pop_anime_index_2 = animeList.pop(2)
# print("Anime list after popping index 2:", animeList)
# print("Popped anime at index 2:", pop_anime_index_2)

# #clear: removes all items from the list, making it an empty list.
# # This method modifies the original list and does not return a new list.
# animeList.clear()
# print("Anime list after clearing:", animeList)

# # sort
# numbers = [5, 2, 9, 1, 5, 6]
# numbers.sort()
# print("Sorted numbers:", numbers)

# #copy
# original_list = ['a', 'b', 'c']
# copied_list = original_list.copy()
# print("Original list:", original_list)
# print("Copied list:", copied_list)

# #iterating over a list (for --- in --)
# myWebtoonReadList = ["Greatest Estate Developer", "The Villainess Reverses the Hourglass", "Solo Leveling", "The Villainess is a Marionette", "Lookism"]
# for webtoon in myWebtoonReadList:
#     print("I am currently reading:", webtoon)

# #for element in range(start, stop, step):
# for webtoon in range(len(myWebtoonReadList)):
#     print(f"Reading:{webtoon} ", myWebtoonReadList[webtoon])

# print("Using range with a step of 2:")
# for webtoon in range(0,len(myWebtoonReadList),2):
#     print(f"Reading:{webtoon} ", myWebtoonReadList[webtoon])

# integers = [1, 2, 3, 4, 5]
# i =0
# #WHILE LOOP

# while i < len(integers):
#     print("Current integer:", integers[i])
#     i += 1

# # in operator
# sentence = "Once upon a time in a land far, far away..."
# print("Is 'time' in the sentence? " + sentence + ": " + str('time' in sentence))
# print("Is 'lime' in the sentence? " + sentence + ": " + str('lime' in sentence))

# side_dishes = ["salad", "fries", "mashed potatoes", "steamed vegetables"]
# print(side_dishes)
# print("Is 'fries' in the side dishes? " + str('fries' in side_dishes))
# print("Is 'rice' in the side dishes? " + str('rice' in side_dishes))


#list unpacking: splits the elements of a list into separate variables.

myBookList = ["The Great Gatsby", "To Kill a Mockingbird", "1984"]

book1, book2, book3 = myBookList
print("Book 1:", book1)
print("Book 2:", book2)
print("Book 3:", book3)

print("Using asterisk (*) to unpack remaining items into a list:")
groceries = ["milk", "bread", "eggs", "cheese", "fruits", "vegetables"]
scan1 , scan2, *rest = groceries
print("Scan 1:", scan1)
print("Scan 2:", scan2)
print("Rest:", rest)


