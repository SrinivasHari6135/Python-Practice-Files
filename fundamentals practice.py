#below script im using addition operation 
sum_1 = 275
sum_2 = 385
print(sum_1+sum_2) #im performing the addition operation '+'
print(type(sum_1))
print(id(sum_1))
"""
above code im using the addition operation,
i want to know the sum_1 which type of data and it's memory location so,
im using the type() function and id()function
"""
account_number = 556745321 # this data type is int data type
account_name = "python developer" # this one is str data type

print(account_number)
print(account_name)

#i'm writting the program that prints a pattern using multiple print statements.

print("* * * * * *")
print("*")
print("*")
print("*")
print("* * * * * *")
print("          *")
print("          *")
print("          *")
print("* * * * * *")


user_name = input("Enter your username :")
"""
with the help of input()function im asking to user enter your details like,
1.user_id
2.user_name
3.user_password
4.user_email
""" 
user_id = input("Enter your id :") 
user_password = input("Enter your password :")
user_email = input("Enter your your email id :")

print(user_name)
print(user_id)
print(user_password)
print(user_email)

#below script im creating varibles of different data types & printed that values

variable_1 = int(356.78)
variable_2 = float(678)
variable_3 = 57
variable_4 = str(variable_3)

print(variable_1)
print(variable_2)
print(variable_4)

print(type(variable_1))
print(type(variable_2))
print(type(variable_4))

#im displaying the memory locations some of above variables

print(id(variable_1))
print(id(user_name)) 
print(id(account_name))
print(id(account_number))
print(id(variable_4))

value_1 = "35" 
value_2 = int(value_1)
print(value_2)
print(type(value_2))

#concatenate two stings and print the results


name_1 = "python "
name_2 = "Developer"
joining = (name_1+name_2)
print(joining)




