#assert - This keyword is used as the debugging tool in Python. It checks the correctness of the code.
# It raises an AssertionError if found any error in the code and also prints the message with an error.

a = 1
b = 0

a = True
b = False

# assert b!=0#

# print(a/b)



# def

# def my_func(a,b):
#     c = a+b
#     print(c)
#
# my_func(10,20)



# class Myclass:
#    #Variables……..
#    def function_name(self):
#       #statements………


#continue


# a = 0
# while a < 4:
#   a += 1
#   if a == 2:
#     continue
#   print(a)



#break


# for i in range(5):
#     if(i==3):
#         break
#     print(i)
# print("End of execution")


# If

# i = 18
# age = int(input("Your age : "))
# if (age < i):
#     print("you are less than 18")
# else:
#     print("Your 18")



# n = 11
# if(n%2 == 0):
#     print("Even")
# else:
#     print("odd")


#elif

# marks = int(input("Enter the marks:"))
# if(marks>=90):
#     print("Excellent")
# elif(marks<90 and marks>=75):
#     print("Very Good")
# elif(marks<75 and marks>=60):
#     print("Good")
# else:
#     print("Faield")


# del

# a=10
# b=12
# del a
# print(b)
# # a is no longer exist
# print(a)

#try, except


# a = 0
# try:
#    b = 1/a
# except Exception as e:
#    print(e)
# finally:
#     print("Division is not possible")


# a=0
# b=5
# try:
#     c = b/a
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print('Finally always executed')


#list

# list = [1,2,3,4,5]
# for i in list:
#     print(i)


#while


# a = 0
# while (a < 5):
#     print(a)
#     a = a + 1


# import


# import math
# print(math.sqrt(30))



#as


# import calendar as cal
# print(cal.month_name[5])


#pass

# class my_class:
#     pass
#
#
# def my_func():
#     pass


#return

# def sum(a, b):
#     c = a + b
#     return c
#
#
# print("The sum is:", sum(25, 15))



#is


# x = 5
# y = 5
#
# a = []
# b = []
# print(x is y)
# print(a is b)
#
# for i in x:
#     print(i)


# global

# def my_func():
#     global a
#     a = 10
#     b = 20
#     c = a + b
#     print(c)
#
#
# my_func()
#
#
# def func():
#     print(a)
#
#
# func()


# nonlocal



# def outside_function():
#     a = 20
#     def inside_function():
#         nonlocal a
#         a = 30
#         print("Inner function: ",a)
#     inside_function()
#     print("Outer function: ",a)
# outside_function()


# lambda


# a = lambda x : x**2
# for i in range(1,6):
#   print(a(i))


# yield


# def fun_Generator():
#     yield 1
#     yield 'Hello Coder'
#     yield 'Hello Coder'
#     yield 'Hello Coder'
#     yield 'Hello Coder'
#     yield 'Hello Coder'
#     yield 'Hello Coder'
#     yield 3
#     yield 3
#     yield 3
#     yield 3

# Driver code to check above generator function
# for value in fun_Generator():
#     print(value)



# with

# with open('file_path', 'w') as file:
#     file.write('hello world !')



# None

def return_none():
    a = 10
    b = 20
    c = a + b


x = return_none()
print(x)