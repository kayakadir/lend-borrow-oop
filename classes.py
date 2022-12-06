# parent class
class Account:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.balance = 0
    def lend(self, amount, receiver): # sending money to someone
        if (amount >= self.balance):
            print('Not enough balance! Balance: £', self.balance)
        else:
            self.balance -= amount
            receiver.balance += amount 
            print(self.name, 'lent to', receiver.name)
    def borrow(self, amount, sender): # get money from someone
        if (amount >= sender.balance):
            print(sender.name, 'has not enough balance! Balance: £', sender.balance)
        else:
            self.balance += amount
            sender.balance -= amount
            print(self.name, 'borrowed from', sender.name)
    def viewBalance(self):
        print(self.name, 'balance: £', self.balance)

# child class
class Member(Account):
    def __init__(self, name, gender):
        super().__init__('Member', name)
        self.gender = gender
    def deposit(self, amount):
        self.balance += amount
        print(self.name, '\'s balance updated: £', self.balance)
    def withdrow(self, amount):
        if (amount >= self.balance):
            print('Not enough balance! Balance: £', self.balance)
        else:
            self.balance -= amount
            print(self.name, '\'s balance updated: £', self.balance)
# child class
class Group(Account):
    def __init__(self, name, monthly_payment, size):
        super().__init__('Group', name)
        self.monthly_payment = monthly_payment # monthly paymeny amount
        self.size = size # total member count
    
