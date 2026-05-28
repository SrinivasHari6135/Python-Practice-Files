while True:
    while True:
        user_name = input("Enter the user name : ")
        user_password = input("Enter the password :")
        if user_password == "vasu@123":
            print("password was matched.....")
            if user_name == "vasu":
                print("username was matched.....")
            else:
                print("Invalid Username......")
                break
        else:
            print("Invaild passwor......")
            break
    

