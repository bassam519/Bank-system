import time
current_time=time.localtime()
formated_time=time.strftime("%d/%m/%Y %H:%M:%S",current_time)

class Bank:
    global formated_time
    def __init__(self):
        self.__accounts=[]
        self.__customers=[]
        self.__transactions=[]

    def get_accounts(self):
        return self.__accounts

    def get_customers(self):
        return self.__customers

    def create_account(self,new_account_number,initial_balance,customer_name):
        account=BankAccount(new_account_number,initial_balance)
        customer = Customer(customer_name,new_account_number,initial_balance)
        self.__accounts.append(account)
        self.__customers.append(customer)

    def remove_account(self,account_number):
        account_found= False
        for account in self.__accounts:
            if account_number == account.get_account_number():
                self.__accounts.remove(account)
                account_found=True
                break
        if not account_found:
            print("Not found account")

        customer_found= False
        for customer in self.__customers:
            if account_number == customer.get_account_number():
                self.__customers.remove(customer)
                customer_found=True
                break
        if not customer_found:
            print("Not found customer")

    def deposit(self,account_number,amount):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                account.set_balance(account.get_balance()+amount)
                self.__transactions.append(f"Deposit amount = ${amount} to account {account_number} at {formated_time}")
                print("Deposit successfully")
                break
            else:
                print("Can't withdraw")
                return
        else:
            print("Account not found")

    def withdraw(self,account_number,amount):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                if account.get_balance() >= amount:
                    account.set_balance(account.get_balance() - amount)
                    self.__transactions.append(f"Withdraw amount = ${amount} to account {account_number} at {formated_time}")
                    print("Withdraw successfully")
                    break
        else:
            print("Account not found")

    def TransferMoney(self,account_number1,account_number2,amount):
        for account2 in self.__accounts:
            if account_number2 == account2.get_account_number():
                if amount<= account2.get_balance():
                    for account1 in self.__accounts:
                        if account_number1 == account1.get_account_number():
                            account1.set_balance(account1.get_balance() + amount)
                    account2.set_balance(account2.get_balance() - amount)
                    self.__transactions.append(f"Transfer {amount} to {account1.get_account_number()} at {formated_time}")
                    print(f"Transfer {amount} successfully")
                    break
        else:
            print("Not found")

    def updateAccountInfo(self,old_account_number,new_account_number,new_balance):
        for account in self.__accounts:
            if account.get_account_number() == old_account_number:
                account.update_accountinfo(new_account_number,new_balance)
                print("Account information updated successfully")
                break
        else:
            print("Not found")

    def updateCustomerInfo(self,old_account_number,new_customer_name,new_account_number):
        for customer in self.__customers:
            if customer.get_account_number() == old_account_number:
                customer.update_customerinfo(new_customer_name,new_account_number)
                print("Customer information updated successfully")
                break
        else:
            print("Not found")

    def display_balance(self):
        counter=1
        for account in self.__accounts:
            print(f"Balance{counter} for customer {account.get_account_number()} -> {account.get_balance()}")
            counter+=1

    def display_transactions(self):
        counter=1
        for transaction in self.__transactions:
            print(f"Transaction{counter} -> {transaction}")
            counter+=1

class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def set_balance(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def update_accountinfo(self,new_account_number,new_balance):
        self.__account_number=new_account_number
        self.__balance=new_balance

class Customer:
    def __init__(self,customer_name,account_number,balance):
        self.__customer_name=customer_name
        self.__account_number=account_number
        self.__balance=balance

    def get_customer_name(self):
        return self.__customer_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def update_customerinfo(self,new_customer_name,new_account_number):
        self.__customer_name=new_customer_name
        self.__account_number=new_account_number

class Transaction:
    def __init__(self,transaction_id,transaction_type,amount,account_number):
        self.__transaction_id=transaction_id
        self.__transaction_type=transaction_type
        self.__amount=amount
        self.__account_number=account_number

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_account_number(self):
        return self.__account_number

    def update_transaction(self,new_transaction_type,new_amount):
        self.__transaction_type=new_transaction_type
        self.__amount=new_amount

class System:
    bank =Bank()

    def main(self):
        while True:
            choice = int(input("\nChoose:\n1-Create account\n2-Remove account\n3-Deposit\n4-Withdraw\n5-Transfer money\n6-Display balance\n7-Display transactions\n8-Update account info\n9-Update customer info\n10-Exit\n\n"))
            if choice == 1:
                account_number=int(input("Enter account number:"))
                balance=int(input("Enter initial balance:"))
                customer_name=input("Enter customer name:")
                self.bank.create_account(account_number,balance,customer_name)
                print("Account added successfully")

            elif choice == 2:
                account_number=int(input("Enter account number:"))
                self.bank.remove_account(account_number)
                print("Account deleted successfully")

            elif choice == 3:
                account_number=int(input("Enter account number:"))
                deposit_balance=int(input("Enter deposit balance:"))
                self.bank.deposit(account_number,deposit_balance)

            elif choice == 4:
                account_number=int(input("Enter account number:"))
                withdraw_balance=int(input("Enter withdraw balance:"))
                self.bank.withdraw(account_number,withdraw_balance)

            elif choice ==5:
                account_number1=int(input("Enter account number1:"))
                amount=int(input("Enter amount:"))
                account_number2=int(input("Enter account number2:"))
                self.bank.TransferMoney(account_number1,account_number2,amount)

            elif choice == 6:
                self.bank.display_balance()

            elif choice == 7:
                self.bank.display_transactions()

            elif choice == 8:
                account_number = int(input("Enter account number to update: "))
                new_account_number = int(input("Enter new account number: "))
                new_balance = float(input("Enter new balance: "))
                self.bank.updateAccountInfo(account_number, new_account_number, new_balance)

            elif choice == 9:
                account_number = int(input("Enter account number to update: "))
                new_account_number = int(input("Enter new account number: "))
                new_customer_name = input("Enter new customer name: ")
                self.bank.updateCustomerInfo(account_number,new_account_number,new_customer_name)

            elif choice == 10:
                break

            else:
                print("Invalid choice")

bank_system =System()
bank_system.main()