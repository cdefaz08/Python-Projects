class Bank():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.active = True
    
    def deposit(self,amount):
        if amount > 0 and self.active == True:
            self.balance += amount
            print(f"You have deposited {amount} on your account {self.name}. Your new balance is {self.balance}")
        else:
            print("acount is not active")

    def withdrawl(self,amount):
        if self.active == True:
            if amount < self.balance:
                self.balance =- amount
                print(f"You withdrawl {amount} form {self.name} your new balance is {self.balance}")    
            else:
                print("Insuficien fonds")
        else:
            print("your acount is not active")

account_1 = Bank("Jhon", 200)
account_2 = Bank("Alex", 700)
account_3 = Bank("Pedro", 100)
account_4 = Bank("Robert", 500)


account_1.deposit(120) 
account_3.withdrawl(1000)

