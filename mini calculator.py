user_input1 = int(input("Enter the number 1 : "))
user_input2 = int(input("Enter the number 2 : "))
operator = input("Enter the operator : ")
if operator == '+':
    print(f"{user_input1}+{user_input2} = {user_input1 + user_input2}")
elif operator == '-':
    print(f"{user_input1}-{user_input2} = {user_input1 - user_input2}")
elif operator == '*':
    print(f"{user_input1}x{user_input2} = {user_input1 * user_input2}")
elif operator == '/':
    print(f"{user_input1}/{user_input2} = {user_input1 / user_input2}")
elif operator == '//':
    print(f"{user_input1}//{user_input2} = {user_input1 // user_input2}")
else:
    print(f"Invalid operator Entered\nEnter the correct operator")



    
    
    
    
    
    
    