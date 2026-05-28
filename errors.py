#value Error
try:
    num_1 = int(input("Enter the number : ")) #im giving the Ten in alphabet letters
    num_2 = int(input("Enter the number : "))
except ValueError as e:
    print(e)

try:
    sample = int("vasu") #try to convert string to int.
    print(sample)
except ValueError as e:
    print(e)

#Type Error
try:
    name_1 = 50
    name_2 = "vasu"
    print(name_1/name_2) # im trying to performing math operations to strings.
except TypeError as e:
    print(e)

#File Not Found Error
try:
    file = open("file.txt",mode='r') #im trying to open and read the not existed file.
    read_file = file.read()
    print(read_file)
    file.close()
except FileNotFoundError as e:
    print(e)
finally:
    print('choose the existed file to read.......')

#Zero Division Error
number_1 = int(input("Enter the number : "))
number_2 = int(input("Enter the number : "))
print(number_1 + number_2)
print(number_1 - number_2)
try:
    print(number_1 / number_2)
except ZeroDivisionError as e:
    print(e)
print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)

#Index Error
sample_list = [5,7,2,8,6]
try:
    print(sample_list[8])
except IndexError as e:
    print(e)

#Key Error
voter_data = {
    "user1":56645,
    "user2":76356,
    "user3":86756,
    "user4":64657,
    "user5":57574
}
print(voter_data["user1"])
print(voter_data["user2"])
print(voter_data["user4"])
try:
    print(voter_data["user6"])
except KeyError as e:
    print(e)
print(voter_data["user3"])
print(voter_data["user5"])

#Attribute Error
number = 145
try:
    number.upper()
except AttributeError as e:
    print(e)

#Over Flow Error
sample_number = 10**900
try:
    converting = float(sample_number)
    print(converting)        
except OverflowError as e:
    print(e)

#Name Error
try:
    print(age)
except Exception as e:
    print(e)

