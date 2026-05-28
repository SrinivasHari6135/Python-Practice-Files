""" 1.) Write a Python program that calculates and prints the sum of the squares of 
numbers from 1 to 5 using a 
for loop
"""
sum_1 = 0
for num_1 in range(1,6):
    result = num_1**2
    print(f"{num_1} square : {result}")
    sum_1 += result
print()    
print(f"sum of 1 To 5 squares is : {sum_1}") 

""" 2.) Write a Python program that uses a while loop to print a countdown from 5 to 1."""

count = 5
while count>0:
    print(count)
    count -=1

""" 3.) Write a Python program to print the multiplication table for a user-specified 
number using a nested for loop."""

table = int(input("Enter number :"))
for i in range(1,11):
    for j in range(1,2):
        print(f"{table} x {i} = {table*i}")

""" 4.) Write a Python program that uses a "for" loop to find the sum of all even 
numbers between 0 and 10 (inclusive)"""

sum = 0
for i in range(11):
    if i%2==0:
        sum +=i
print(sum) 

""" 5.) Calculate the sum of all numbers from 1 to a given number"""

sum_5 = 0
value_1 = int(input("Enter number :"))
for i in range(1,value_1+1):
    sum_5 +=i
print(f"sum of 1 to 20 numbers is {sum_5}")

""" 6.) Display numbers from a list using loop"""


number_5 = [225,325,425,525,625,725,825]
for i in number_5:
    if i==725:
        print(i)

number_6 = [50,100,150,200,250,300,350]
for i in number_6:
    print(i)


""" 7.) Display numbers from -10 to -1 using for loop"""

for i in range(-10,0):
    print(i)

""" 8.) Write a Python program to print the cube of all numbers from 1 to a given 
number"""

cube = int(input("Enter cube number :"))
for i in range(1,cube+1):
    print(f"{i} cube = {i**3}")

