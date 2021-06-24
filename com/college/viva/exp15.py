# WAP to Create a List, Add Elements into List and reverse the List.

listName = []               # Creating List.
temp = []                   # Creating Another List.
listName.extend("ABC")      # Adding Element using extend().
listName.insert(1, "A1")    # Adding Element using insert().
listName.insert(2, "A2")
listName.append("D")        # Adding Element using append().
temp.extend(listName)
listName.reverse()          # Reversing List using reverse().
print("The reversed of list", temp, " is ", listName)

# Performed by Gaurav Amarnani, Roll No. 21, CO6IA.
