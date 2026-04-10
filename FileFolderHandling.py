#File and folder handling
# info = open("users.txt", mode="r")
# info = open("users.txt", "r")
# info = open("users.txt")
# print(info)
# print(info.name)
# print(info.mode)
# print(info.readable())
# print(info.closed)
#=====================================================
# userinfo = open("userinfo.txt", "w")
# userinfo.write("Name: John Doe\n")
# userinfo.write("Age: 30\n")
#===================================================
# friends_list = open("friends.txt", "w")
# friends = ["Alice\n", "Bob\n", "Charlie\n", "David\n", "Eve\n"]
# friends_list.writelines(friends)
# friends_list.close()
# =====================================================
# friend_list = open("friends.txt", "r")
# print(friend_list.read())
# print(friend_list.read(16))
# print(friend_list.readline())
# ==============================
# data = open("data.txt", "r")
# #read the data
# content = data.read()
# # print(content)

# # write to moredata.txt
# moredata = open("moredata.txt","w")
# moredata.write(content)

#==================================================
import os 

# print(os.getcwd())
# os.mkdir("newfolder")
# os.mkdir("Movies/Netflix")
# os.makedirs("Movies/Netflix/The Office")
# os.rename("newfolder", "Movies")
# os.rmdir("Movies/Netflix/The Office")
# os.remove("data.txt")
# os.chdir("Movies/Netflix")
# print(os.getcwd())
# os.removedirs("Movies/Netflix")