import random

class Bank:
    def __init__(self):
        self.users = []
        self.admins = []
        self.loan_feature_enabled = True

class BankAccount:
    def __init__(self, name, email, account_type):
        if account_type == 's' :
            self.account_number = f'AC/Savings{random.randint(10000, 99999)}'
        elif account_type == 'c':
            self.account_number = f'AC/Current{random.randint(10000, 99999)}'
        else:
            print("Invalid account type")
        self.name = name
        self.email = email
        self.account_type = account_type
        self.balance = 0
        self.transactions = []
        self.loan_taken = 0
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        print(f"Deposited ${amount} successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            print(f"Withdrew ${amount} successfully.")

    def check_balance(self):
        print(f"Available balance: ${self.balance}")

    def check_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.loan_taken += amount
            self.balance += amount
            self.transactions.append(f"Loan Taken: ${amount}")
            self.loan_count += 1
            print(f"Loan of ${amount} taken successfully.")
        else:
            print("You have reached the maximum limit of loans.")

class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def create_account(self, bank, name, email, account_type):
        account = BankAccount(name, email, account_type)
        bank.users.append(account)
        print("Successfully created account.")

    def delete_account(self, bank, account_number):
        found_account = None
        for user in bank.users:
            for account in user.accounts:
                if account.account_number == account_number:
                    found_account = account
                    break
            if found_account:
                break
        
        if found_account:
            bank.users.remove(user)
            print("Account deleted successfully.")
        else:
            print("Account not found.")


    def see_all_accounts(self, bank):
        print("All User Accounts:")
        for user in bank.users:
            for account in user.accounts:
                print(f"Name: {user.name}, Account Number: {account.account_number}")

    def total_balance(self, bank):
        total_balance = sum(account.balance for user in bank.users for account in user.accounts)
        print(f"Total Available Balance: ${total_balance}")

    def total_loan_amount(self, bank):
        total_loan = sum(account.loan_taken for user in bank.users for account in user.accounts)
        print(f"Total Loan Amount: ${total_loan}")

    def toggle_loan_feature(self, bank, status):
        bank.loan_feature_enabled = status
        if status:
            print("Loan feature enabled.")
        else:
            print("Loan feature disabled.")

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.accounts = []

    def create_account(self, bank, name, email, account_type):
        account = BankAccount(name, email, account_type)
        self.accounts.append(account)
        bank.users.append(self)
        print(f'Account created successfully. Your account number is: {account.account_number}')


    def deposit(self, account, amount):
        account.deposit(amount)

    def withdraw(self, account, amount):
        account.withdraw(amount)

    def check_balance(self, account):
        account.check_balance()

    def check_transactions(self, account):
        account.check_transactions()

    def take_loan(self, account, amount):
        account.take_loan(amount)


bank = Bank()

admin = Admin('admin', 'adminPass')
bank.admins.append(admin)

user1 = User('user1', 'pass1')
user2 = User('user2', 'pass2')
bank.users.append(user1)
bank.users.append(user2)

while True:
    print(" ")
    print("Welcome to the Bank Management System")
    print(" ")

    option = input("Are you an Admin or a User? (A/U): ").upper()

    if option == 'A':
        admin_name = input("Enter Admin Name: ")
        admin_password = input("Enter Admin Password: ")
        isAdmin = None
        for admin in bank.admins:
            if admin.name == admin_name and admin.password == admin_password:
                isAdmin = admin
                break

        if isAdmin:
            print(" ")
            print("Enter your options:")
            print("1 : Create Account")
            print("2 : Delete Account")
            print("3 : See All User Accounts")
            print("4 : Check Total Available Balance")
            print("5 : Check Total Loan Amount")
            print("6 : Toggle Loan Feature")
            print("7 : Logout")

            ch = int(input("Enter Option: "))

            if ch == 1:
                name = input("Enter User Name: ")
                email = input("Enter Email: ")
                account_type = input("Enter Account Type (s/c): ")
                isAdmin.create_account(bank, name, email, account_type)

            elif ch == 2:
                account_number = input("Enter Account Number to Delete: ")
                isAdmin.delete_account(bank, account_number)

            elif ch == 3:
                isAdmin.see_all_accounts(bank)

            elif ch == 4:
                isAdmin.total_balance(bank)

            elif ch == 5:
                isAdmin.total_loan_amount(bank)

            elif ch == 6:
                status = input("Enter '0' to enable or '1' to disable loan feature: ")
                if status == '0':
                    isAdmin.toggle_loan_feature(bank, True)
                elif status == '1':
                    isAdmin.toggle_loan_feature(bank, False)

            elif ch == 7:
                print("Logged out.")
                break
        else:
            print("Admin authentication failed. Please try again.")

    elif option == 'U':
        user_name = input("Enter User Name: ")
        user_password = input("Enter User Password: ")
        isUser = None
        for user in bank.users:
            if user.name == user_name and user.password == user_password:
                isUser = user
                break

        if isUser:
            print("\nOptions:")
            print("1 : Create Account")
            print("2 : Deposit Amount")
            print("3 : Withdraw Amount")
            print("4 : Check Available Balance")
            print("5 : Check Transaction History")
            print("6 : Take Loan")
            print("7 : Transfer Amount")
            print("8 : Logout")

            ch = int(input("Enter Option: "))

            if ch == 1:
                name = input("Enter User Name: ")
                email = input("Enter Email: ")
                account_type = input("Enter Account Type (s/c): ")
                isUser.create_account(bank, name, email, account_type)

            if ch == 2:
                account_number = input("Enter Account Number: ")
                amount = float(input("Enter Amount to Deposit: "))
                found_account = None
                for account in isUser.accounts:
                    if account.account_number == account_number:
                        found_account = account
                        break
                if found_account:
                    isUser.deposit(found_account, amount)
                else:
                    print("Account not found.")


            if ch == 3:
                account_number = input("Enter Account Number: ")
                amount = float(input("Enter Amount to Withdraw: "))
                found_account = None
                for account in isUser.accounts:
                    if account.account_number == account_number:
                        found_account = account
                        break
                if found_account:
                    isUser.withdraw(found_account, amount)
                else:
                    print("Account not found.")


            if ch == 4:
                account_number = input("Enter Account Number: ")
                found_account = None
                for account in isUser.accounts:
                    if account.account_number == account_number:
                        found_account = account
                        break
                if found_account:
                    isUser.check_balance(found_account)
                else:
                    print("Account not found.")


            if ch == 5:
                account_number = input("Enter Account Number: ")
                found_account = None
                for account in isUser.accounts:
                    if account.account_number == account_number:
                        found_account = account
                        break
                if found_account:
                    isUser.check_transactions(found_account)
                else:
                    print("Account not found.")


            if ch == 6:
                account_number = input("Enter Account Number: ")
                amount = float(input("Enter Loan Amount: "))
                found_account = None
                for account in isUser.accounts:
                    if account.account_number == account_number:
                        found_account = account
                        break
                if found_account:
                    isUser.take_loan(found_account, amount)
                else:
                    print("Account not found.")


            if ch == 7:
                print("Can't implemented")

            elif ch == 8:
                print("Logged out.")
                break

    else:
        print("Invalid Option. Please enter a valid option")
