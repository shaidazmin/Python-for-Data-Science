# Days = {"Monday", "Tuesday", "Tuesday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
# print(Days)
# print(type(Days))
# print("looping through the set elements ... ")
# for i in Days:
#     print(i,end='')


# months = {("January","February", "March", "April", "May", "June"),'November', 'devember'}
# print("\nprinting the original set ... ")
# print(months)
#
# print("\nAdding other months to the set...");
# months.add("July");
# months.add ("August");
#
#
# print("\nPrinting the modified set...");
# print(months)
# print("\nlooping through the set elements ... ")
# for i in months:
#     print(i)


# Months = set(["January","February", "March", "April", "May", "June"])
# print("\nprinting the original set ... ")
# print(Months)
# print("\nupdating the original set ... ")
# Months.update(["July","August","September","October"]);
# print("\nprinting the modified set ... ")
# print(Months);


# months = set(["January","February", "March", "April", "May", "June"])
# print("\nprinting the original set ... ")
# print(months)
# print("\nRemoving some months from the set...");
# months.discard("January");
# months.discard("May");
# print("\nPrinting the modified set...");
# print(months)
# print("\nlooping through the set elements ... ")
# for i in months:
#     print(i)


# months = set(["January","February", "March", "April", "May", "June"])
# print("\nprinting the original set ... ")
# print(months)
# print("\nRemoving some months from the set...");
# months.remove("January");
# months.remove("May");
# print("\nPrinting the modified set...");
# print(months)


# Months = set(["January","February", "March", "April", "May", "June"])
# print("\nprinting the original set ... ")
# print(Months)
# Months.pop()
# print(Months)
# Months.pop()
# print(Months)


# Months = set(["January","February", "March", "April", "May", "June"])
# print("\nprinting the original set ... ")
# print(Months)
# print("\nRemoving all the items from the set...");
# Months.clear()
# print("\nPrinting the modified set...")
# print(Months)


# Months = set(["January","February", "March", "April", "May", "June"])
# print("\nprinting the original set ... ")
# print(Months)
# print("\nRemoving items through discard() method...");
# Months.discard("Feb"); #will not give an error although the key feb is not available in the set
# print("\nprinting the modified set...")
# print(Months)
# print("\nRemoving items through remove() method...");
# Months.remove("Jan") #will give an error as the key jan is not available in the set.
# print("\nPrinting the modified set...")
# print(Months)




# Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}
# Days2 = {"Friday","Saturday","Sunday"}
# print(Days1|Days2)
# print(Days1.union(Days2))#printing the union of the sets


# Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}
# Days2 = {"Monday","Tuesday","Sunday", "Friday"}
# print(Days1&Days2)
# print(Days1.intersection(Days2))#prints the intersection of the two sets


# set1 = {1,2,3,4,5,6,7}
# set2 = {1,2,20,32,5,9}
# set3 = set1.intersection(set2)
# print(set3)


# a = {"Devansh", "bob", "castle"}
# b = {"castle", "dude", "emyway"}
# c = {"fuson", "gaurav", "castle"}
#
# a.intersection_update(b, c)
#
# print(a)




# Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
# Days2 = {"Monday", "Tuesday", "Sunday"}
# print(Days1-Days2) #{"Wednesday", "Thursday" will be printed}
# print(Days1.difference(Days2)) #{"Wednesday", "Thursday" will be printed}



#Symmetric Difference of two sets
# a = {1,2,3,4,5,6}
# b = {1,2,9,8,10}
# c = a^b
# print(c)
#
# a = {1,2,3,4,5,6}
# b = {1,2,9,8,10}
# c = a.symmetric_difference(b)
# print(c)


# Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
# Days2 = {"Monday", "Tuesday"}
# Days3 = {"Monday", "Tuesday", "Friday"}
#
# # Days1 is the superset of Days2 hence it will print true.
# print(Days1 > Days2)
#
# # prints false since Days1 is not the subset of Days2
# print(Days1 < Days2)
#
# # prints false since Days2 and Days3 are not equivalent
# print(Days2 == Days3)



# Frozenset = frozenset([1,2,3,4,5])
# print(type(Frozenset))
# print("\nprinting the content of frozen set...")
# for i in Frozenset:
#     print(i);
# Frozenset.add(6) #gives an error since we cannot change the content of Frozenset after creation



# Dictionary = {"Name":"John", "Country":"USA", "ID":101}
# print(type(Dictionary))
# Frozenset = frozenset(Dictionary); #Frozenset will contain the keys of the dictionary
# print(type(Frozenset))
# for i in Frozenset:
#     print(i)




# Example - 1: Write a program to remove the given number from the set.

# my_set = {1,2,3,4,5,6,12,24}
# print(my_set)
# my_set.discard(int(input("enter number : ")))
#
# print(my_set)



# Example - 2: Write a program to add multiple elements to the set.

# set1 = {(1,2,4,"John","CS")}
# set1.update(("Apple",("Mango"),"Grapes"))
# print(set1)



# Example - 3: Write a program to find the union between two set.

# set1 = set(["Peter","Joseph", 65,59,96])
# set2  = set(["Peter",1,2,"Joseph"])
# # set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)




# set1 = set(["Peter", "James", "Camroon", "Ricky", "Donald"])
# set2 = set(["Camroon", "Washington", "Peter"])
# set3 = set(["Peter"])
#
# issubset = set1 >= set2
# print(issubset)
# issuperset = set1 <= set2
# print(issuperset)
# issubset = set3 <= set2
# print(issubset)
# issuperset = set2 >= set3
# print(issuperset)