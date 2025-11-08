# SACCO Member Wallet

# Step 1: Create a member dictionary
Members = {}

def register(name,balance):
    Members[name] = balance
    print(f"\nDear, {name} your balance is {balance}")

def withdrawals(name, amount):
    if name in Members:
        if Members[name] >= amount:
            Members[name] -= amount
            print(f"Successfully withdrawn {amount} from account. New Balance: KES {Members[name]}")
        else:
            print("Insufficient funds!")

def deposit(name, amount):
    if name in Members:
        Members[name] += amount
        print(f"You Have Deposited: KES {amount} in your account.")
    else:
        print("Member Not Found!")

def balance_check(name):
    if name in Members:
        print(f"You Balance is {Members[name]}")        

def loan(name, amount):
    if name in Members:
        Members[name] -= amount
        print(f"You have successfully got the a loan of Kes {amount}")
        print("Should be paid in 3 Months!")
    else:
        print("You are Not a Member!")


def get_registration_details():
    name = input("Enter Name: ")
    depositing_amount = int(input("Enter the Deposit Amount: "))
    return name, depositing_amount

register_details = get_registration_details()


register(register_details[0], register_details[1])
withdrawals(register_details[0], 200)
deposit(register_details[0], 300)
balance_check(register_details[0])
