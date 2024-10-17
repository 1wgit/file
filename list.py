####listing###

my_list = [5, 6, 1, 7, 9, 0]
print(my_list)
empty_list =[]
print(empty_list)
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)

###Accessing elememt#####


print(my_list)
firstName_element = my_list[0]
Last_element = my_list[-1]
print(firstName_element)
print(Last_element)

#######modifing element#####
my_list[0]=10
print(my_list)

########addingelement#######
my_list.append(6) # adding 6 at end
print(my_list)

#########insert###
my_list.insert(1,15)
print(my_list)

#####findingindex of element######
print("findingindex of element")
print(my_list)
index_of_seven = my_list.index(7)

########find no. of occurance#######
count_of_five = my_list.count(True)
print(count_of_five)



##########sort list##########
my_list = [5, 6, 1, 9]
my_list.sort()
print(my_list)


my_list_sorted = sorted(my_list, reverse=True)#optional reverse
print(my_list_sorted)
print(my_list)
########reverse list######
my_list.reverse()
print(my_list)

##########copy LIst#######
another_copy = my_list[:]
print(another_copy)

#########clearList#######

my_list.clear()
print(my_list)

#######joininglist##########

list1 = [1, 2, 3]
list2= [4, 5]
combined_list = list1 + list2
print(combined_list)


###slicing###
my_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = my_list[1:3]
print(sub_list)
