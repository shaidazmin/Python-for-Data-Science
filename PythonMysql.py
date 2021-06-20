import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database ="python_db")
cur =myconn.cursor()
# cur.execute("show databases")
# for x in cur:
#     print(x)

# dbs = cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, dept_id int not null)")


sql = "insert into Employee(name, id, salary, Dept_id) values(%s,%s,%s,%s)"


val = ("John", 111, 25000.00, 201)

inputValue = []

# for i in range(4):
#     inputValue.append(input("Enter Value : "))


# print(inputValue)

# try:
#     cur.execute(sql, tuple(inputValue))
#     myconn.commit()
# except:
#     print("something went wrong")


try:
    cur.execute("select * from Employee")
    result = cur.fetchall()
    for x in result:
        print(x)


except:
    myconn.rollback()

# with open("writhingFile.txt", 'r') as tst:
#     for i in tst:
#         print(i)


myconn.close()

