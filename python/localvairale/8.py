amount = int(input("enter amount: "))
dep = int(input("enter the deposit amount: "))
wd = int(input("enter the withdraw amount: "))
def deposit(amt):
    global amount
    amount = amount + amt
    print(amt, "deposit")
def withdraw(amt):
    global amount
    amount = amount - amt
    print(amt, "withdraw")
print("balance=",amount)
deposit(dep)
withdraw(wd)
print("balance=",amount)
