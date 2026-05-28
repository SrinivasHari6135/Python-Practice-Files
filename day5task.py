""" 1.) Write a Python program that takes a character as input and checks whether it is a vowel or not
Use the if-else statement."""

character = input("Enter character :")
vowels = "aeiouAEIOU"
if character in vowels:
    print(f"{character} is vowel")
else:
    print(f"{character} is not vowel")


""" 2.) Write a program that takes an age as input and classifies the person into 
one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older"""



age = float(input("Enter your age :"))
if age <=0:
    print(f"Enter correct age")
elif age >= 65:
    print(f"you are senior person your age is {age}")
elif age >=0 and age <=12:
    print(f"you are child person your age is {age}")
elif age >=13 and age <=17:
    print(f"you are teenager person your age is {age}")
elif age >=18 and age <=64:
    print(f"you are adult person your age is {age}")


""" 3.) Write a program that takes an integer as input and classifies it as positive, 
negative, or zero. Use the if-elif-else statement."""


num_1 = int(input("Enter number :"))
if num_1<0:
    print(f"{num_1} it is negative number")
elif num_1>0:
    print(f"{num_1} it is positive number")
else:
    print(f"it is zero")


""" 4.) Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400. """

leap_year = int(input("Enter number :"))
if(leap_year %4==0 and leap_year %100!=0) or leap_year %400==0 :
    print(f"{leap_year} it is lear")
else:
    print(f"{leap_year} it is not leap year")


""" 5.) Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation. """


num_5 = int(input("Enter number 1 :"))
num_6 = int(input("Enter number 2 :"))
operator = input("Enter operator :")

if operator =="+":
    print("Result =",num_5 + num_6)
elif operator == "-":
    print("Result =",num_5 - num_6)
elif operator == "*":
    print("Result =",num_5 * num_6)
elif operator == "/":
    print("Result =",num_5 / num_6)
else:
    print("Enter correct operator.....")


""" 6.) Rewrite the following code using the short-hand 
if statement:
x = 8 ,if x % 2 == 0: result = "Even" else: result = "Odd"""
num_7 = int(input("Enter number :"))
print(("even number")if num_7%2==0 else("odd number"))

""" 7.) Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as input."""

original_price = int(input("Enter price :"))
discount = int(input("Enter discount :"))
discount_amount = original_price * discount/100
original_price -= discount_amount
print("Final Selling Price =",original_price)

""" 8.) Write a program that calculates the Body Mass Index (BMI) using the 
formula: BMI = weight (kg) / (height (m))^2. The program should take 
weight and height as input. """

weight = int(input("Enter your weight :"))
height = int(input("Enter your height :"))
bmi = weight/(height)**2
print("Your body mass index is :",bmi)



