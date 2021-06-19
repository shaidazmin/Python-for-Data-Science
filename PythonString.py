# Using single quotes
# str1 = 'Hello Python'
# print(str1)
# # Using double quotes
# str2 = "Hello Python"
# print(str2)
#
# # Using triple quotes
# str3 = '''''Triple quotes are generally used for
#     represent the multiline or
#     docstring'''
# print(str3)


# str = "JAVATPOINT"
# # Start Oth index to end
# print(str[0:])
# # Starts 1th index to 4th index
# print(str[1:5])
# # Starts 2nd index to 3rd index
# print(str[2:4])
# # Starts 0th to 2nd index
# print(str[:3])
# #Starts 4th to 6th index
# print(str[4:7])
#
# print(str[:10])



# str = 'JAVA T POINT'
#
# print(str[::-1])
# print(str[-1])
# print(str[-3])
# print(str[-2:])
# print(str[-4:-1])
# print(str[-7:-2])
# # Reversing the given string
# print(str[::-1])
# print(str[-10::])
# print(str[-10])


# str = "Hello"
# str1 = " world"
# print(str*3) # prints HelloHelloHello
# print(str+str1)# prints Hello world
# print(str[4]) # prints o
# print(str[2:4]); # prints ll
# print('w' in str) # prints false as w is not present in str
# print('wo' not in str1) # prints false as wo is present in str1.
# print(r'C://python37') # prints C://python37 as it is written
# print("The string str : %s"%(str)) # prints The string str : Hello
#
#
# print('H' in str)

# print('''''They said, "What's there?"''')
#
# # escaping single quotes
# print('They said, "What\'s going on?"')
#
# # escaping double quotes
# print("They said, \"What's going on?\"")



# print("C:\\Users\\DEVANSH SHARMA\\Python32\\Lib")
# print("This is the \n multiline quotes")
# print("This is \x48\x45\x58 representation")


# print(R"C:\\Users\\DEVANSH SHARMA\\Python32")


# Using Curly braces
# print("{} and {} both are the best friend".format("Devansh", "Abhishek"))
#
# # Positional Argument
# print("{1} and {0} best players ".format("Virat", "Rohit"))
#
# # Keyword Argument
# print("{a},{b},{c}".format(a="James", b="Peter", c="Ricky"))
#
#
# print(" %d + %.2f = is an decilaml"%(10,2.10));
# print(" {0} + {1} = is an decilaml".format(int(10),float(20)));


#
# Integer = 10;
# Float = 1.290
# String = "Devansh"
# print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))
#


# python String Method ...............................................



# 1. capitalize()


# Python capitalize() function example
# # Variable declaration
# str = "hello shaid azmin?"
# # Calling function
# str2 = str.capitalize()
#
# # Displaying result
# print("Old value:", str)
# print("New value:", str2)



# 2. casefold()



# # Python casefold() function example
# # Variable declaration
# str = " WE ARE LEARING JAVA PROGRAMMING β 1245 54"
# # Calling function
# str2 = str.casefold()
# # Displaying result
# print("Old value:", str)
# print("New value:", str2)
#
#
# # Python casefold() function example
# # Variable declaration
# str = "JAVATPOINT - β"
# # Calling function
# str2 = str.casefold()
# # Displaying result
# print("Old value:", str)
# print("New value:", str2)



# 3. center(width ,fillchar)




# Python center() function example
# Variable declaration
# str = "Hello"
# # Calling function
# str2 = str.center(11,'!')
# # Displaying result
# print("Old value:", str)
# print("New value:", str2)


# 4.   Count()

# Python count() function example
# Variable declaration
# str = "Hello Javatpoint"
#
# str2 = str.count('a')
# # Displaying result
# print("occurences : ", str2)
#
#
# # Python count() function example
# # Variable declaration
# str = "ab bc ca de ed ad da ab bc ca"
# oc = str.count('a')
# # Displaying result
# print("occurences:", oc)
#
# # Python count() function example
# # Variable declaration
# str = "ab bc ca de ed ad da ab bc ca"
# oc = str.count('a', 1)
# # Displaying result
# print("occurences:", oc)



# Python count() function example
# Variable declaration
# str = "taaareq mamun"
#
# print(len(str))
# oc = str.count('a',1,5)
# # Displaying result
# print("occurences:", oc)


# 5. Encode()

# import base64
#
#
# # Python encode() function example
# # Variable declaration
# str = "this is string example....wow!!!";
#
# str2 = base64.standard_b64encode(str)
#
#     print(str)




#6 endswith() .......

# Python endswith() function example
# Variable declaration
# str = "Hello this is javatpoint."
# isends = str.endswith(".")
# # Displaying result
# print(isends)
#
# # Python endswith() function example
# # Variable declaration
# str = "Hello this is javatpoint."
# isends = str.endswith("is")
# # Displaying result
# print(isends)
#
# # Python endswith() function example
# # Variable declaration
# str = "Hello this is javatpoint."
# isends = str.endswith("is",10)
# # Displaying result
# print(isends)
#
#
# # Python endswith() function example
# # Variable declaration
# str = "Hello this is javatpoint."
# isends = str.endswith("is",0,13)
# # Displaying result
# print(isends)



# 7.  expandtabs().................

#
# # Python endswith() function example
# # Variable declaration
# str = "Welcome \t to \t the \t Javatpoint."
# # Calling function
# print(str)
# str2 = str.expandtabs()
# # Displaying result
# print(str2)
#
#
# # Python endswith() function example
# # Variable declaration
# str = "Welcome \t to \t the \t Javatpoint."
# # Calling function
# str2 = str.expandtabs(1)
# str3 = str.expandtabs(2)
# str4 = str.expandtabs(4)
# # Displaying result
# print(str2)
# print(str3)
# print(str4)


# 8  find().......................

# # Python find() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.find("o")
# # Displaying result
# print(str2)
#
# # Python find() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.find("is")
# # Displaying result
# print(str2)
#
#
# # Python find() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.find("t")
# str3 = str.find("t",20,25)
# # Displaying result
# print(str2)
# print(str3)


# # Python find() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.find("t")
# str3 = str.find("t",25)
# # Displaying result
# print(str2)
# print(str3)



# 9. format()........


#
# # Python format() function example
# # Variable declaration
# str = "Java"
# str2 = "C#"
# # Calling function
# str3 = "{} and {} both are programming languages".format(str,str2)
# # Displaying result
# print(str3)





# 10, index() ..................................


# # Python index() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.index("at")
# # Displaying result
# print(str2)
#
#
# # Python index() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.index("ate")
# # Displaying result
# print(str2)


# # Python index() function example
# # Variable declaration
# str = "Welcome to the Javatpoint."
# # Calling function
# str2 = str.index("p",19,21)
# # Displaying result
# print("p is present at :",str2,"index")



# 11. isalnum()...........................


# # Python isalnum() function example
# # Variable declaration
# str = "Welcome"
# # Calling function
# str2 = str.isalnum()
# # Displaying result
# print(str2)
#
#
# # Python isalnum() function example
# # Variable declaration
# str = "Welcome"
# # Calling function
# str2 = str.isalnum()
# # Displaying result
# print(str2)
#
# # Python isalnum() function example
# # Variable declaration
# str = "Welcome123" # True
# str3 = "Welcome 123" # False
# # Calling function
# str2 = str.isalnum()
# str4 = str3.isalnum()
# # Displaying result
# print(str2)
# print(str4)
#
# # Python isalnum() function example
# # Variable declaration
# str = "1234ssasf56"
# # Calling function
# str2 = str.isalnum()
# # Displaying result
# print(str2)



# 12. isalpha() ............................

# # Python isalpha() method example
# # Variable declaration
# str = "JavatpointIs"
# # Calling function
# str2 = str.isalpha()
# # Displaying result
# print(str2)


# 13. isdecimal()  ...................


# # Python isdecimal() method example
# # Variable declaration
# str = "12455.0"
# # Calling function
# str2 = str.isdecimal()
# # Displaying result
# print(str2)


# 14. isdigit().....................

# # Python isdigit() method example
# # Variable declaration
# str = '123a45'
# # Calling function
# str2 = str.isdigit()
# # Displaying result
# print(str2)


# 15. isidentifier()...............

# Python isidentifier() method example
# Variable declaration
# str = "14abcdef122"
#
# print(str.capitalize())
# # Calling function
# str2 = str.isidentifier()
# # Displaying result
# print(str2)


# 16. islower()  ...............


# # Python islower() method example
# # Variable declaration
# str = "javatpoiNt"
# # Calling function
# str2 = str.islower()
# # Displaying result
# print(str2)


# 17.isnumeric()..................


# # Python isnumeric() method example
# # Variable declaration
# str = "1545"
# # Calling function
# str2 = str.isnumeric()
# # Displaying result
# print(str2)


# 18. isprintable(). .........................

# # Python isprintable() method example
# # Variable declaration
# str = "Hello, Javatpoint 445645"
# str2 = "Learn Java here\n"
# str3 = "\t Python is a programming language"
# # Calling function
# str4 = str.isprintable()
# str5 = str2.isprintable()
# str6 = str3.isprintable()
# # Displaying result
# print(str4)
# print(str5)
# print(str6)


# 19. isupper()  ................


# # Python isupper() method example
# # Variable declaration
# str = "WELCOME TO JAVATPOINT a"
# # Calling function
# str2 = str.isupper()
# # Displaying result
# print(str2)


# 20. isspace() ......................




# isspace() method returns true for all whitespaces like:
#
# ' ' - Space
# '\t' - Horizontal tab
# '\n' - Newline
# '\v' - Vertical tab
# '\f' - Feed
# '\r' - Carriage return


# Python isspace() method example
# Variable declaration
# str = " " # string contains space
# if str.isspace() == True:
#     print("It contains space 1")
# else:
#     print("Not space 1")
# str = "ab cd ef \n"
# if str.isspace() == True:
#     print("It contains space 2")
# else:
#     print("Not space 2")
# str = "\t \r \n"
# if str.isspace() == True:
#     print("It contains space 3")
# else:
#     print("Not space 3 ")



# 21. istitle()....................



# Python istitle() method example
# # Variable declaration
# str = "How Are You" # True
# # Calling function
# str2 = str.istitle()
# # Displaying result
# print(str2)
# str = "Hello javatpoint"    # False
# str2 = str.istitle()
# print(str2)


# 22.  join()..........................



# Python join() method example
# Variable declaration
# str = ":"   # string
# list = ['1','2','3']    # iterable
# # Calling function
# str2 = str.join(list)
# # Displaying result
# print(str2)
# print(type(list))
#
#
#
# # Python join() method example
# # Variable declaration
# str = ""   # string
# list = ['J','a','v','a','t','p','o','i','n','t']    # iterable
# # Calling function
# str2 = str.join(list)
# # Displaying result
# print(str2)
# print(type(list))
#
#
# # Python join() method example
# # Variable declaration
# str = "->"   # string
# list = {'Java','C#','Python'}    # iterable
# # Calling function
# str2 = str.join(list)
# # Displaying result
# print(str2)
# print(type(list))
#
#
# # Python join() method example
# # Variable declaration
# dic =  {'key1': 1, 'key2': 2}
# str = ' & '
# # Calling function
# str = str.join(dic)
# # Displaying result
# print(str)
# print(type(dic))


# 23. len()....................



#
# strA = 'Python'
# print(len(strA))
#
#
# listA = ['Python', 'C', 'C++', 'Java']
# print(len(listA))
#
#
# dictA = {
#     'name': 'Phill', 'university': 'GTU', 'ID': 1107
# }
# print(len(dictA))


# 24. ljust()..........................


# Python ljust() method example
# Variable declaration
# str = 'Javatpoint'
# # Calling function
# str = str.ljust(20)
# # Displaying result
# print(str)
#
#
# # Python ljust() method example
# # Variable declaration
# str = 'Javatpoint'
# # Calling function
# str = str.ljust(15,"$")
# str2 = "Hellloooooo".rjust(15,"$")
# # Displaying result
# print(str)
# print(str2)


# 25. lower().....................



# # Python lower() method example
# # Variable declaration
# str = "Javatpoint"
# # Calling function
# str = str.lower()
# # Displaying result
# print(str)
#
#
# # Python lower() method example
# # Variable declaration
# str = "Welcome To JAVAtpoint, WWW.JAVATPOINT.COM"
# # Calling function
# str = str.lower()
# # Displaying result
# print(str)


# 26. lstrip().....................................

#
# # Python lstrip() method example
# # Variable declaration
# str =  "  Javatpoint   is One \t of the hub of      knowledge"
# # Calling function
# str2 = str.lstrip()
# # Displaying result
# print(str)
# print(str2)
#
# print(" Javatpoint   is One \t of the hub of      knowledge".rstrip(" "))
#
#
# # Python lstrip() method example
# # Variable declaration
# str =  "$$$$-Javatpoint-$$$$"
# # Calling function
# str2 = str.lstrip('$')
# # Displaying result
# print(str)
# print(str2)
#
#
# # Python lstrip() method example
# # Variable declaration
# str =  "http://www.javatpoint.com"
# # Calling function
# str2 = str.lstrip('http://w .')
# # Displaying result
# print(str)
# print(str2)


# 27.   partition() method example  ........................


# # Python partition() method example
# # Variable declaration
# str = "Java is a programming language"
# # Calling function
# str2 = str.partition("m")
# # Displaying result
# print(str2)
# # when seperate from the start
# str2 = str.partition("Java")
# print(str2)
# # when seperate is the end
# str2 = str.partition("language")
# print(str2)
# # when seperater is a substring
# str2 = str.partition("av")
# print(str2)
#
# # Python partition() method example
# # Variable declaration
# str = "Java is a programming language"
# # Calling function
# str2 = str.partition("not")
# # Displaying result
# print(str2)


# 28. maketrans()................................

#
# mystr = 'Most'
# mappingtbl = mystr.maketrans('t','P')
# print(mappingtbl)
#
# print(mystr.translate(mappingtbl))
#
#
# mystr = 'Most'
# mappingtbl = mystr.maketrans('Mts','Hdl')
# print('Mapping table: ', mappingtbl)
#
# newstr = mystr.translate(mappingtbl)
# print('Translation: ', newstr)



# 29. replace() method example.......................



# # Python replace() method example
# # Variable declaration
# str = "Java is a programming language"
# # Calling function
# str2 = str.replace("Java","C")
# # Displaying result
# print("Old String: \n",str)
# print("New String: \n",str2)


# # Python replace() method example
# # Variable declaration
# str = "Java C C# Java Php Python Java"
# # Calling function
# str2 = str.replace("Java","C#",1) # replaces all the occurences
# # Displaying result
# print("Old String: \n",str)
# print("New String: \n",str2)
# # Calling function
# str2 = str.replace("Java","C#",1) # replaces first occurance only
# # Displaying result
# print("\n Old String: \n",str)
# print("New String: \n",str2)




# 30. rfind() method example  ............. Right Rinder ..............


# # Python rfind() method example
# # Variable declaration
# str = "Learn Java it Java tooo demandaable"
# # calling function
# str2 = str.rfind("Java")
# # displaying result
# print(str2)
#
#
# # Python rfind() method example
# # Variable declaration
# str = "It is technical tutorial"
# # calling function
# str2 = str.rfind("t")
# # displaying result
# print(str2)
#
#
# # Python rfind() method example
# # Variable declaration
# str = "It is technical tutorial"
# # calling function
# str2 = str.rfind("t",5) # Only starting index is passed
# # displaying result
# print(str2)
# str2 = str.rfind("t",5,10) # Start and End both indexes are passed
# print(str2)




# 31. rindex() method example ......Right Index ..............


# # Python rindex() method example
# # Variable declaration
# str = "It is technical tutorial"
# # calling function
# str2 = str.rindex("is") # No start and end is given
# # displaying result
# print(str2)
#
#
#
# # Python rindex() method example
# # Variable declaration
# str = "It is technical tutorial"
# # calling function
# str2 = str.rindex("t") # No start and end is given
# # displaying result
# print(str2)
# str2 = str.rfind("t",5,15) # Start is end both are given
# print(str2)


# 32.  split()................



# # Python split() method example
# # Variable declaration
# str = "Java is a programming language"
# # Calling function
# str2 = str.split()
# # Displaying result
# print(str)
# print(str2)
#
# str = "Java is a programming language"
# # Calling function
# str2 = str.split('Java')
# # Displaying result
# print(str2)
#
#
# str = "Java is a programming language"
# # Calling function
# str2 = str.split('a')
# # Displaying result
# print(str)
# print(str2)
#
# str = "Java is a programming language"
# # Calling function
# str2 = str.split('a', 1)
# # Displaying result
# print(str2)
#
# str2 = str.split('a', ' ')
# # Displaying result
# print(str2)
#
#
# # Python splitlines() method example
# # Variable declaration
# str = "Java \n is a programming \r language for \r\n  software development"
# # Calling function
# str2 = str.splitlines() # returns a list having splitted elements
# # Displaying result
# print(str2)
# # getting back list to string
# print("".join(str2)) # now it does not contain any line breaker character



# 33.  zfill()..................


# # Python zfill(width) method
# # Declaring variables
# text = "Zfill Example"
# # Calling Function
# str2 = text.zfill(20)
# # Displaying result
# print(str2)
#
# # Python zfill(width) method
# # Declaring variables
# val = "+100"
# val2 = "-200"
# val3 = "--Rohan--"
# # Calling Function
# str2 = val.zfill(10)
# str3 = val2.zfill(10)
# str4 = val3.zfill(10)
#
# # Displaying result
# print(str2)
# print(str3)
# print(str4)


# 34.  rpartition() method example  ..................


# Python rpartition() method example
# # Variable declaration
# str = "Java is a programming language"
# # Calling function
# str2 = str.rpartition("is")
# # Displaying result
# print(str2)
# # seperator is at begining
# str2 = str.rpartition("Java")
# print(str2)
# # seperator at ent
# str2 = str.rpartition("language")
# print(str2)
# # when seperater is a substring
# str2 = str.rpartition("av")
# print(str2)