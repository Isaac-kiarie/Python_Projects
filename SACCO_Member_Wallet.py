# SACCO Member Wallet

# Step 1: Create a member dictionary
Members = {}

def register(name,balance):
    Members[name] = balance
    print(f"Dear, {name} your balance is {balance}")

def withdrawals(name, amount):
    if name in Members:
        Members[name] -= amount
        print(f"Successfully withdrawn {amount} from account. New Balance: KES {Members[name]}")
    else:
        print("Sorry Member Not Found!")

def deposit(name, amount):
    if name in Members:
        Members[name] += amount
        print(f"You Have Deposited: KES {amount} in your account.")
    else:
        print("Member Not Found!")

def balance_check(name):
    if name in Members:
        print(f"You Balance is {Members[name]}")        

register("Isaac", 4000)
withdrawals("Isaac", 200)
deposit("Isaac", 300)
balance_check("Isaac")
