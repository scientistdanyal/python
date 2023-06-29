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


clients = []

options = 1
while options != 5:
    print("1. Enter Client Data")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Search Client Data")
    print("5. Exit")
    options = int(input("Enter your choice: "))

    if options == 1:
        client = Bank_acc(0, "", 0)
        client.data()
        clients.append(client)
        print("Client data added successfully!")

    elif options == 2:
        acc_no = int(input("Enter account number: "))
        found = False
        for client in clients:
            if client.acc_no == acc_no:
                client.deposit()
                found = True
                break
        if not found:
            print("Client not found!")

    elif options == 3:
        acc_no = int(input("Enter account number: "))
        found = False
        for client in clients:
            if client.acc_no == acc_no:
                client.withdraw()
                found = True
                break
        if not found:
            print("Client not found!")

    elif options == 4:
        acc_no = int(input("Enter account number: "))
        found = False
        for client in clients:
            if client.acc_no == acc_no:
                print("Client Data:")
                print("Account Number:", client.acc_no)
                print("Owner Name:", client.owner_name)
                print("Balance:", client.balance)
                found = True
                break
        if not found:
            print("Client not found!")

    else:
        print("Goodbye!")


print(clients.type)