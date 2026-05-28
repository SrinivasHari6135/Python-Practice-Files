# 1.) write a program that prints your name.

my_name = "srinivas"
print(my_name) # with help of print() function im display my name on the screen.
print(type(my_name)) #im using type() function to know my_name is which type of class.

''' 2.) create a python script with both single-line and multi-line comments explaining
       purpose of the script.
''' 
# below code im performing the addition,multiplication and divisions operations

sem_1_marks = 87
sem_2_marks = 91
sem_3_marks = 79
sem_4_marks = 85
result_1 = sem_1_marks+sem_2_marks+sem_3_marks+sem_4_marks

'''adding all sem marks with the help of + operation and after adding all sem marks
im performing the division operation to minimize the marks and after that performing the 
multiplication and addition operation to finalize the marks.
'''
print(result_1)
result_2 = result_1/4
print(result_2)
final_result = (result_2*2)+100
print(final_result)

# 3.) define a list containing three difierent data types.

sample_list = [55,46,56.34,"srinivas","pythonlife,87.56,98,25"]
print(sample_list)
print(type(sample_list))

# 4.) define a set containing employee id's.

employee_id = {"srinivas","hari","vasu","vasu","python","pythonlife","python","fast","learn"}
print(employee_id)
print(type(employee_id))

# 5.) concatenate two strings and print the result.
brand_name = "iqoo "
product_name = "neo 9 pro"
print(brand_name+product_name) #im concatenating the two strings with help of + operation.

# 6.) repeat a string five times and display the output.
name_1 = "vasu,"
name_2 = (name_1+" ")*5 # im printing the vasu name for 5 times with the help of multiplication.
print(name_2)

# 7.) create a variable with a name that is a python keyword,what happens.

#if = "python"
#print(if) 
'''we can't use the (if) as a variable because it is a python special keyword,in python we can't
use the python special keywods for a variables '''

# 8.) declare two variables, one storing an integer and the other a string, print their values.

value_1 = 85
value_2 = "65"
print(value_1)
print(type(value_1))
print(value_2)
print(type(value_2))

# 9.) convert a float to an integer and integer to a string and print the result.

value_3 = 56.78
print(type(value_3))
value_4 = int(value_3)
print(value_4)
print(type(value_4))

value_5 = 675
print(type(value_5))
value_6 = str(value_5)
print(value_6)
print(type(value_6))


# 10.) take the user's age as input and print a message using that input.

user_age = input("Enter your age :")
print(user_age)












