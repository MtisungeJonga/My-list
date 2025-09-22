#empty list 
my_list = []
print("Before Append:",my_list)

#Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After Append:", my_list)

#inserting the value 15 at the 2nd position
my_list[1]= 15
print(my_list)

#Extending the list
my_list = [10,15,30,40]
print("List1:" ,my_list)

another_list = [50,60,70]
print("List2:", another_list)

my_list.extend(another_list)
print("List after extend:", my_list)

#Deleting the last element
del my_list[-1]
print("List after deleting:",my_list)

#Sorting in ascending order
my_list.sort()
print("List after sorting:", my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)