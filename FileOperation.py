#
# fileRead = open("jokes.txt","r")
#
# for i in fileRead:
#     print(i)
#
# print(fileRead.readline())
#
# fileRead.close()


newFile = open("writingFile.txt", 'a')

#

newFile.write(input("Write : "))


newFile = open("writingFile.txt", 'r')

for i in newFile:
    print(i)

print(newFile.readline())

newFile.close()

with open("writingFile.txt") as file:
    for i in file:
        print(i)


