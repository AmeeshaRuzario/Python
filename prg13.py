class Account:
    def __init__(self, number):
        self.__number = number
        self.__balance = 100

    def deposit(self, amount):
        self.__balance += amount
        print("account balance is:", self.__balance)

    def withdraw(self, amount):
        if self.__balance-amount < 100:
            print("low balance cant withdraw")
        else:
            self.__balance -= amount
            print("account balance:", self.__balance)

    def getbalance(self):
        return self.__balance


acclist = []
accnolist = []
while True:
    print("\nEnter")
    print("1:Account creation\n2:Deposit\n3:Withdraw")
    print("4:Get highest balance\n5:Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        number = int(input("enter the account number:"))
        if number in accnolist:
            print("account already exists")
        else:
            new = Account(number)
            acclist.append(new)
            accnolist.append(number)
    elif ch == 2:
        number = int(input("enter the account no:"))
        if number in accnolist:
            amount = float(input("enter the amount to deposit:"))
            index = accnolist.index(number)
            acclist[index].deposit(amount)
        else:
            print("no account")
    elif ch == 3:
        number = int(input("enter the account no:"))
        if number in accnolist:
            amount = float(input("enter the amount:"))
            index = accnolist.index(number)
            acclist[index].withdraw(amount)
        else:
            print("no account")
    elif ch == 4:
        ballist = []
        for obj in acclist:
            ballist.append(obj.getbalance())
        if len(ballist) == 0:
            print("no data")
        else:
            high = max(ballist)
            index = ballist.index(high)
            print("highest balance is:", high)
            print("account no is:", accnolist[index])
    else:
        break
