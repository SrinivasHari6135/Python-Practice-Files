user_name = input("Enter your name :")
user_age = input("Enter your age :")
print(f"Hello my dear friends my name is {user_name} and i'm {user_age} years old!")
#above code im using the f"string" function to detailing the output on the display.

voter_list = ["hari","veera","ram","srinivas","python","pythonlife","kumar"]
print("siva" in voter_list) # im using membership operator(in) to konw the sive name is in the list or not.
print("hari" in voter_list)
print("veera" not in voter_list)

"""i want know veera name is included or not included in the list so,i'm performing membership
 not in operator."""

print("srinivas" in voter_list)
print("pythonlife" in voter_list)

sample_list = [1,2,3,4,5,6,7,8,9,10]
print(5 in sample_list)
print(15 not in sample_list)
print(6 in sample_list)
print(5 in sample_list)


length_value =int(input("Enter the length value :"))
width_value = int(input("Enter the width value :"))
area_of_rectangle = length_value * width_value

print("Area of Rectangle :",area_of_rectangle)


num_1 = 75
num_2 = 10
print(num_1+num_2)
num_1+=10
print(num_1)
num_1-=10
print(num_1)
num_2+=10
print(num_2)
num_2+=20
print(num_1+num_2)

celsius = int(input("Enter celsius value :"))
fahrenheit = (celsius+9/5)+32
print(fahrenheit)


principle = 25000
time = 5
rate_of_interest = 20
simple_interest = (principle*time*rate_of_interest)/100 #si formula = (ptr)/100
print(simple_interest)
print("Total amount with interest :",simple_interest+principle)


person_name_1 = input("Enter your first name :")
person_name_2 = input("Enter your last name :")
final_name = person_name_1+" "+person_name_2
print(final_name)


value_1 = 0.621 # 1 kilometer = 0.621 miles
value_1*= 6 # im giving the 6 kilometers
"""im converting the kilometers to miles, variable of value_1 consist miles and 
variable of value_2 consist 6 kilometers """
print("6 Kilometers =",value_1,"miles")



