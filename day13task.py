""" 1.) Write a Python function square_all(numbers) that takes a list of numbers as input 
and returns a new list containing the square of each number in the input list. Use the 
map() function with a lambda function to implement this."""
#1st approach
list1 = [1,2,3,4,5,6,7,8,9]
def square(a):
    return a**2
result = map (square,list1)
print(list(result))

#2nd approach
result1 = map(lambda a:a**2,list1)
print(list(result1))


""" 2.) Write a Python function filter_positive(numbers) that takes a list of numbers as 
input and returns a new list containing only the positive numbers from the input list. Use the 
filter() function with a lambda function to implement this."""
#1st approach
list_2 = [1,-3,2,5,6,-10,-15,10,9,25,-28,16,-26,8]
def positive(b):
    return b>=0
result_2 = filter(positive,list_2)
print(list(result_2))
#2nd approach
result_3 = filter(lambda c:c>0,list_2)
print(list(result_3))


""" 3.) Write a Python function calculate_factorial(n) that calculates the factorial of a given number n. Use the 
reduce() function with an appropriate lambda function to implement this."""

# factorial = int(input("Enter the number : "))
from functools import reduce
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(5))

""" 4.) Write a Python function count_vowels(string) that takes a string as input and 
returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() 
function with an appropriate lambda function to implement this."""

def count_vowels_1(string):
    vowel = "aeiouAEIOU"
    return reduce(lambda count,i:count+1 if i in vowel else count,string,0)
print(count_vowels_1("srinivas"))