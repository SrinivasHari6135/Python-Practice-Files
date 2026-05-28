# sets task

""" 1.) Write Python code to find and print the intersection of the following two sets:
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
inter_section = set_1.intersection(set_2)
print(inter_section)

""" 2.) Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(union_set)

""" 3.) Write Python code to find and print the elements present in set3 but not in set4"""
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
print(set3.difference(set4))

""" 4.) Write Python code to find and print the symmetric difference of the following 
two sets:
set_3 = {1, 2, 3, 4, 5}
set_4= {4, 5, 6, 7, 8} """

set_3 = {1, 2, 3, 4, 5}
set_4 = {4, 5, 6, 7, 8}
print(set_3.symmetric_difference(set_4))

""" 5.) Write Python code to check if the element 3 is present in the set my_set
my_set = {1, 2, 3, 4, 5} """

my_set = {1, 2, 3, 4, 5}
presence = my_set.isdisjoint("3")
print(presence)

# tuples task

""" 1.) Write a program that creates a tuple containing three 
elements: your name, your age, and your favorite color. Then print the tuple."""

sample_tup = ("srinivas", 24, "blue")
print(sample_tup)

""" 2.) Write a program that creates a tuple containing the 
days of the week. Then, print the third element of the tuple."""

days_tuple = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days_tuple[2])

""" 3.)  Write a program that creates two tuples, one 
containing odd numbers from 1 to 5 and another containing even numbers 
from 2 to 6. Concatenate these two tuples and print the result."""

odd_tuple = (1, 3, 5)
even_tuple = (2, 4, 6)
tuple_concatenation = odd_tuple + even_tuple
print(tuple_concatenation)

""" 4.)  Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle."""

tuple_7 = (10,5)
length,width = tuple_7
area_of_rectangle = length*width
print(area_of_rectangle)


""" 5.)  Write a program that checks if a given element exists in a tuple."""

tuple_5 = ("python","vasu","pythonlife","scale","pen")
element_presence = "pythonlife" in tuple_5
print(element_presence)

""" 6.) Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items."""

items = [("Apple", 99.79), ("Banana", 96.28), ("Milk", 49.15), ("Sugar", 25.25), ("Salt", 30)]
print(f"Item\t\tPrice")
print("="*20)
total = 0
for i,j in items:
    print(f"{i}\t\t{j:.2f}")
    total += j
print("="*20)
print(f"Total\t\t{total:.2f}")