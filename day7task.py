""" 1.) Write a Python program that takes a list of numbers as input numbers = [25, 30, 20, 40, 15, 25]
and prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100"""

number_1 = [25,20, 30, 10,20, 40, 15, 25, 30]
sum_1 = 0
for i in number_1:
    sum_1 += i
    if sum_1>100:
        break

print(sum_1)


""" 2.) Write a Python script that uses a for loop to iterate through numbers from 1 to 
600. Print only the odd numbers, skipping the even ones using the continue statement."""

for i in range(1,601):
    if i%2==0:
        continue
    print(i)


""" 3.) Write a Python script that checks if a number is even or odd. If the number is 
even, print "Even"; if odd, do nothing (use the pass statement)."""
    
number_2 = int(input("Enter number :"))
if number_2 %2==0:
    print(f"{number_2} is a Even Number")
    if number_2 %2!=0:
        pass


""" 4.) Write a Python script that iterates through a list of words. If the word is "break," exit the loop using the 
break statement. If the word is "skip," skip the rest of the code for the current iteration using the 
continue statement. For any other word, print the word"""

words_1 = ["srinivas", "vasu", "skip", "hari", "break", "veera"]
for i in words_1:
    if i == "skip":
        continue
    if i == "break":
        break
    
    print(i)

print(f"last iteration : {i}")