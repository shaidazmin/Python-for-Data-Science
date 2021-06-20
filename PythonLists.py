# a = [1, 'Helon', 'Rakib', 344]
# b = [1, 'Helon', 'Rakib', 344]
#
# print(a==b)



# emp = ["John", 102, "USA"]
# Dep1 = ["CS",10]
# Dep2 = ["IT",11]
# HOD_CS = [10,"Mr. Holding"]
# HOD_IT = [11, "Mr. Bewon"]
# print("printing employee data...")
# print("Name : %s, ID: %d, Country: %s"%(emp[0],emp[1],emp[2]))
# print("printing departments...")
# print("Department 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s, ID: %s"%(Dep1[0],Dep2[1],Dep2[0],Dep2[1]))
# print("HOD Details ....")
# print("CS HOD Name: %s, Id: %d"%(HOD_CS[1],HOD_CS[0]))
# print("IT HOD Name: %s, Id: %d"%(HOD_IT[1],HOD_IT[0]))
# print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))




# list = [1,2,3,4,5,6,7]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# # Slicing the elements
# print(list[0:6])
# # By default the index value is 0 so its starts from the 0th element and go for index -1.
# print(list[:])
# print(list[2:5])
# print(list[1:6:2])




# list = [1, 2, 3, 4, 5, 6]
# list2= [1, 2, 3, 4, 5, 6]






# print(list)
# # It will assign value to the value to the second index
# list[2] = 10
# print(list)
# # Adding multiple-element
#
# userList = ['primary', 'data', 'car', 'bike']
# print('primary' and 'data' and 'car'  in userList)
#
# size = int(input("Enter the list size : "))
#
#
# for i in range(size):
#     userList.append(int(input("Enter Value : ")))
#
#
# print(userList)
# i = int(input())
# userList.remove(userList[i])
# print(userList)
#
# print('primary' in userList)
#
# list[1:3] = [89, 78]
# print(list)
# # It will add value at the end of the list
# list[-1] = 25
# print(list)


# list = [1, 2, 3]
# list2= [1, 2, 3, 4, 5, 6]
#
# userList = ['primary', 'data', 'car', 'bike']
#
#
# print(len(userList))
#
#
# if len(list) > len(userList):
#     print(list+userList+list2)
# else:
#     print(userList)
#
# print(min(list and list2 and userList))
# print(min(list2))
# print(min(userList))
# print(min(list))



# Example: 1- Write the program to remove the duplicate element of the list.

# list1 = [1,2,2,3,55,98,65,65,13,29]
# # Declare an empty list that will store unique values
# list2 = []
# for i in list1:
#     if i in list2:
#         list2.append(i)
# print(list2)


# import  math
# list1 = [3,4,5,9,10,12,24]
# sum = 1
# for i in list1:
#     sum = math.sqrt(sum+i)
# print("The sum is:",sum)


# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9,2,4, 5,1,10]
# for y in list1:
#     for x in list2:
#         if y == x:
#             print("The common element is:",x)