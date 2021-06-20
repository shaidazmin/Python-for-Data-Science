
import pandas

# with open("t.csv") as test:
#     for i in test:
#         print(i.split(','))
#         token = i.split(',')
#         table = token[0]
#         print(table)


# dic = {}
#
# with open('t.csv', mode='r') as test:
#     for row in test:
#         dic['name'] = row.split(",")[0]
#         dic['dep'] = row.split(",")[1]
#         dic['bith'] = row.split(",")[2]
#
#     for name, dep, bith in dic.items():
#         print(f"name => {name} , dep => {dep}, brth => {bith} ")




# for name, dep, bith in dic.items():
#     print(f"name => {name} , dep => {dep}, brth => {bith} ")


print(pandas.read_csv("t.csv"))

