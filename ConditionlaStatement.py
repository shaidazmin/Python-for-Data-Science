# Conditonal statement ...........

#
# num = int(input("enter the number : "))
#
#
# if num%2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd ")
#
# if num > 80:
#     print(num)
# elif num > 70:
#     print(num)
# elif num > 60:
#     print(num)
# elif num > 50:
#     print(num)
# else:
#     print("Dhoinca")



# Looppppppppp..................



# name = 'Shaid Azmin'
#
# for n in name:
#    print(n+n)

# list = [1,2,3,4,5,6,7,8,9,10]
# n = 5
# for i in list:
#     n = n*i
#
# print(n)



# list = [10,30,23,43,65,12]
# sum = 0
# for i in list:
#     sum = sum+i
# print("The sum is:",sum)

# range() function .........

# import math
#
# for i in range(10):
#     print(i*i- math.sqrt(i*i+i),end = ' ')


# n = int(input("Enter the number "))
# for i in range(1,11,1):
#     c = n*i
#     print(n,"*",i,"=",c)



# n = int(input("Enter the number "))
#
# for i in range(1,n):
#     if(i%2 != 0):
#         print("Odd : ", i)
#     else:
#         print("Even : ", i)


# list = ['Peter','Joseph','Ricky','Devansh']
# for i in range(len(list)):
#     print("Hello",list[i],"how are you?")


# Nested Loop ........


# User input for number of rows
# rows = int(input("Enter the rows:"))
# # Outer loop will print number of rows
# for i in range(0,rows+1):
# # Inner loop will print number of Astrisk
#     for j in range(i):
#         print("*",end = '')
#     print()


# for i in range(1, rows+1):
#     for j in range(i):
#         if(j == 2):
#             continue
#         print(j+i,end='')
#     print()



# for i in range(0,5):
#     print(i)
#     continue
#     # break
#
# else:print("for loop is exhausted");
# print("The loop is broken due to break statement...came out of the loop")

# for i in range(0,5):
#     print(i)
# else:
#     print("for loop completely exhausted, since there is no break.")






# while looooppppppppppppppppppp..........................................


# prints all letters except 'a' and 't'


# i = 0
# str1 = 'java t point'
#
# while i < len(str1):
#     if str1[i] == ' ':
#         i += 1
#         continue
#     print('Current Letter :', str1[i])
#     i += 1

# The control transfer is transfered
# when break statement soon it sees t
# i = 0
# str1 = 'javatpoint'
#
# while i < len(str1):
#     if str1[i] == 't':
#         i += 1
#         break
#     print(str1[i], end='')
#     i += 1



# An empty loop
# str1 = 'javatpoint'
# i = 0
#
# while i < len(str1):
#     i += 1
#
# print('Value of i :', i)


# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print('This is pass block')
#    print('Current Letter :', letter)
#
# print
# 'Good bye!'


# i=1
# #The while loop will iterate until condition becomes false.
# while(i<=10):
#     print(i)
#     i=i+1



# i=1
#
# number = int(input("Enter the number:"))
# while i<=10:
#     print("%d X %d = %d \n"%(number,i,number*i))
#     i = i+1


# terms = int(input("Enter the terms "))
# # first two intial terms
# a = 0
# b = 1
# count = 0
#
# # check if the number of terms is Zero or negative
# if (terms <= 0):
#     print("Please enter a valid integer")
# elif (terms == 1):
#     print("Fibonacci sequence upto", limit, ":")
#     print(a)
# else:
#     print("Fibonacci sequence:")
#     while (count < terms):
#         print(a, end=' ')
#         c = a + b
#         # updateing values
#         a = b
#         b = c
#
#     count += 1





