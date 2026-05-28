""" 1.) Write Python code to add a new key-value pair to the following dictionary.
        my_dict_1 = {'name': 'python', 'age': 25} """

my_dict_1 = {'name': 'python', 'age': 25}
new_data = {'city': 'west godavari'}
my_dict_1.update(new_data)
print(my_dict_1)

""" 2.) Write Python code to access and print the value associated with the key 'price' in 
the following dictionary: product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200} """

#1st approach to access the "1200" value. 
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get("price"))

#2nd approach to access the "1200" value.
print(product_info["price"])

""" 3.) Write Python code to remove the key-value pair with the key 'city' from the 
following dictionary: my_dict_2 = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}"""

my_dict_2 = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict_2.pop("city")
print(my_dict_2)

""" 4.) Write Python code to print all the keys present in the following dictionary:
        my_dict_3 = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'} """

my_dict_3 = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict_3.keys())

""" 5.) Write Python code to print all the values present in the following dictionary:
       my_dict_4 = {'name': 'python', 'age': 25, 'city': 'tanuku'} """

my_dict_4 = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict_4.values())