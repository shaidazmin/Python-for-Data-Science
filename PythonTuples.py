# creating Tupple ..........


# T1 = (101, "Peter", 22)
# T2 = ("Apple", "Banana", "Orange")
# T3 = 10, 20, 30, 40, 50
#
# print(type(T1))
# print(type(T2))
# print(type(T3))

# tup1 = ("JavaTpoint")
# print(type(tup1))
# #Creating a tuple with single element
# tup2 = ("JavaTpoint",)
# print(type(tup2))


# tuple1 = (10,10,20,10, 20, 30, 40, 50, 60)
#
# print(tuple1)
#
# count = 0
# for i in tuple1:
#     print("tuple1[%d] = %d "%(count, i),end='')
#     count = count+1



tuple1 = tuple(input("Enter the tuple elements ..."))
print(tuple1)
count = 0
for i in tuple1:
    print("tuple1[%d] = %s"%(count, i))
    count = count+1