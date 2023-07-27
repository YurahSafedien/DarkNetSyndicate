# BANK CALCULATIONS
'''
These calculations include depositing and withdrawing money. We also end up with a new balance.
Deposit = yay!!!
Withdrawing = oof! we broke x_x
'''

# calculate deposit balance
def calculate_deposit(current_amount, dep_amount):
    new_balance = current_amount + dep_amount
    print("R", dep_amount, " has been deposited. Your new balance is R", new_balance, ".")
    current_amount = new_balance
    return current_amount

# calculate withdraw balance
def calculate_withdrawal(current_amount, withdrawal_amount):
    new_balance = current_amount - withdrawal_amount
    print("R", withdrawal_amount, " has been withdrawn. Your new balance is R", new_balance, ".")
    current_amount = new_balance
    return current_amount
