""" 1.) Write Python code to reverse the order of elements in the given list 
Print the reversed list. my_list = [10, 20, 30, 40, 50, 11]"""

# 1st approach to reverse the order of elements in my_list......

my_list = [10, 20, 30, 40, 50, 11]
print(my_list[::-1]) #im using the slicing method to reverse the order of elements in my_list

# 2nd approach to reverse the order of elements in my_list......

my_list_1 = [10, 20, 30, 40, 50, 11]
my_list_1.reverse()
print(my_list_1)


""" 2.) Given two lists list1 and list2 , find and print the common elements between them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8] """

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
empty_list =[]
for i in list_1:
    for j in list_2:
        if i==j:
            empty_list.append(i)

print(empty_list)


""" 3.) Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5] """

original_list = [1, 2, 2, 3, 4, 4, 5]
empty_list_1 = []
for i in original_list:
    if i not in empty_list_1:
        empty_list_1.append(i)

print(empty_list_1)


""" 4.) Remove duplicate elements from the given list duplicated_list and print the list
without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]"""

# 1st approach 

duplicated_list = [1, 2, 2, 3, 4, 4, 5]
empty_list_2 =[]
for i in duplicated_list:
    if i not in empty_list_2:
        empty_list_2.append(i)

print(empty_list_2)


""" 5.) Write a Python script that concatenates two lists and prints the result."""

list_3 = [2,5,8,3,7,9]
list_4 = [1,3,6,9,4,8]
result_list = list_3+list_4
print(result_list)


""" 6.) Write a Python script that repeats a list three times and prints the result."""

list_5 = [2,5,8,3,7,1,5,8]
print(list_5*3)

""" 7.) Write a Python script that removes the elements at even indices from a list."""

empty_list_5 = []
list_6 = [1,2,3,5,7,8,9,10,15,16,18,19,20,22,23,25,26,29,30,32,35]
for i in list_6:
    if i %2!=0:
        empty_list_5.append(i)

print(empty_list_5)

""" 8.) Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list. """
# 1st approach
list_8 = [5,2,7,3,4,8,9,1]
list_8.insert(0,'10, 11, 12')
print(list_8)

#2nd approach
list_9 = [10,11,12]
list_10 = [5,2,7,3,4,8,9,1]
print(list_9+list_10)

""" 9.) Create a list of squares of numbers from 1 to 10. """

#1st approach
empty_list_7 = []
for i in range(1,11):
    result_10 = i**2
    empty_list_7.append(result_10)

print(empty_list_7)

#2nd approach
result_13 = [i**2 for i in range(1,11)] #im using list comprehension method.......
print(result_13)


""" 10.) Generate a list of even numbers from 1 to 20. """

result_14 = [i for i in range(1,21) if i%2==0]
print(result_14)

""" 11.)  Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"] """

word_1 = ["apple", "banana", "cherry", "date"]
word_length = []
for i in word_1:
    word_length.append(len(i))
print(word_length)