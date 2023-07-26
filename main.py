
# HOME FORUM

# if email is found in TEXTFILE and password matches said email , print(Log In successful)
# !=, print("Login Failed") -- should have a "Forgot password" and or "sign up" as options

# LOG IN FORUM

# user_email_login = input("Enter your email/username: ")
# user_password_login = input("Enter your password: ") 
    
# ACCOUNT CREATION
account_creation = input("Do you want to create an account? Press 'y' for yes and 'n' for no").lower()

if account_creation =='y':
    # no numbers are allowed in first and last name
    user_first_name = input("Enter your first name: ")
    user_last_name = input("Enter your last name: ")

    # validation for the "@" symbol
    user_email_create = input("Enter your email address: ")

    # future updates: may add a specila character, uppercase and lowercase characters as well as numbers
    user_password_create = input("Enter your password:")


    # comfirm_user_password == user_password , != then print("Passwords are not matching.Re-enter your password")
    comfirm_user_password_create  =input("Comifrm password:")
    
    if user_email_create  != comfirm_user_password_create :
        print("Your passwords are not matching. Please re-enter your passwords.")  
    else:
        print("Accoumt created!")
    

# OPTION FORUM

# user_option -->> stores whether the user wants to wthdrawl and or deposit
user_option = input("Hi, do you wish to withdrawl or deposit?Press d-deposit or w-withdrawl:")

if user_option == 'w':
    # withdrawl_user_input -->> the amount  the user wishes to withdrawl
    withdrawl_user_input= input("how much do you wish to withdrawl?")
elif user_option == 'd':
    # deposit_user_input -->> the amount  the user wishes to deposit
    deposit_user_input= input("how much do you wish to deposit?")
else:
    print("Invalid input. Try again.")

# ignore above until further evalution
# sincierly team leader
    