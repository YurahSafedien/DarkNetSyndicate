# INPUT VALIDATION
'''
Input validation is vital for checking for possible nulls and invalid outputs, etc. Wrote this comment 
because the heading felt lonely x.x
'''

# check for validity of option
def get_option_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            if value == 'w' or value == 'd':
                return value
            else:
                print("Invalid input. Enter valid option.")
        else:
            print("Input cannot be empty. Please try again.")

# check for invalid withdrawal input
def get_valid_withdrawal_input(prompt, current_value):
    while True:
        try:
            value = input(prompt)
            if value.strip():
                value = float(value)
                if value > 0 and value <= current_value:
                    value = round(value, 2) 
                    return value
                else:
                    print("Invalid input. Please enter a sufficient integer amount.")
            else:
                print("Input cannot be empty. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer amount.")
                        
# check for invalid deposit input
def get_valid_deposit_input(prompt, current_value):
    while True:
        try:
            value = input(prompt)
            if value.strip():
                value = float(value)
                if value > 0:
                    value = round(value, 2) 
                    return value
                else:
                    print("Invalid input. Please enter a sufficient integer amount.")
            else:
                print("Input cannot be empty. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer amount.")