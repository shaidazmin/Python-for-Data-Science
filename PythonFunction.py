# defining the function
# def change_list(list1):
#     list1.append(20)
#     list1.append(30)
#     print("list inside function = ", list1)
#
#
# # defining the list
# list1 = [10, 30, 40, 50]
#
# # calling the function
# change_list(list1)
# print("list outside function = ", list1)
#

# def printme(*names):
#     print("type of passed argument is ",type(names))
#     print("printing the passed arguments...")
#     for name in names:
#         print(name)
# printme(10)
# printme(10)
# printme(10)
# printme(10)
#
#
#
# def food(**kwargs):
#     print(kwargs)
# food(a="Apple")
# food(a="Apple")
# food(a="Apple")
# food(fruits="Orange", Vagitables="Carrot")
# food(fruits="Orange", Vagitables="Carrot")
# food(fruits="Orange", Vagitables="Carrot")



# Lambda


x = lambda aaa,b,c : aaa*aaa+b+c
print(x(10,10,20))


inp_list = ['t','u','t','o','r','i','a','l']
result = list(filter(lambda x: x=='t' , inp_list))

value =  list(filter(lambda a : 'a' in inp_list, inp_list))

print(value)

print(result)


inp_list = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x%2==0 , inp_list))

print(result)