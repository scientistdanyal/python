class Bank_acc:
    def __init__(self, acc_no, owner_name, balance):
        self.acc_no = acc_no
        self.owner_name = owner_name
        self.balance = balance

    def data(self):
        self.owner_name = input("Enter your name: ")
        self.acc_no = int(input("Enter account number: "))
        self.balance = int(input("Enter your balance: $"))


    def deposit(self):
        dep = int(input("How much do you want to deposit: $"))
        self.balance += dep
        print("Your new balance is: $", self.balance)

    def withdraw(self):
        wit = int(input("How much do you want to withdraw: $"))
        if wit > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= wit
            print("Your new balance is: $", self.balance)



danyal = Bank_acc(0, "", 0)

danyal.data()

print(danyal.owner_name, danyal.acc_no, danyal.balance)

danyal.deposit()


danyal.withdraw()

print(danyal.owner_name, danyal.acc_no, danyal.balance)
