class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount 
            print(f"Deposited {amount} into account of {self.account_holder} su saldo actual es: {self.balance}")
        else:
            print("Account is not active")

    def withdraw(self, amount):
        if self.is_active:
            if amount > self.balance:
                print("Insufficient funds")
                return
            else:
                self.balance -= amount
                print(f"withdraw {amount} from account of {self.account_holder} su saldo actual es: {self.balance}")
        else:
            print("Account is not active")
            
    def close_account(self):
        self.is_active = False
        print(f"Account of {self.account_holder} has been closed")

    def activate_account(self):
        self.is_active = True
        print(f"Account of {self.account_holder} has been activated")

    def get_balance(self):
        return self.balance

account_1 = BankAccount("John", 1000)
account_2 = BankAccount("Jane", 2000)
account_3 = BankAccount("Doe", 3000)

#llamada a los metodos
account_1.deposit(100)
account_2.withdraw(200)
account_3.close_account()
account_3.deposit(50)
account_3.activate_account()
account_3.withdraw(100)