# class Human:
#     def __init__(self, head, body):
#         print("Defalut Constractor")
#         self.head = head
#         self.body = body
#
#     def getData(self):
#         return {"head":self.head, "body":self.body}
#     def getName(self):
#         return f"head : {self.head},"
#
#
#
# man = Human('Round', "square")
# print(man.getData())
# print(man.getName())

# from abc import ABC, abstractmethod


class Car():
    def __mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
