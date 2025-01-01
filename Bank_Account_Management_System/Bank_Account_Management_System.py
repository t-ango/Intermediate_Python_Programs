'''
Bank Account Management System

This program simulates a simple banking system with the ability to manage accounts, perform transactions, and record transaction histories.

## Classes and Features

### 1. `Account`
Represents a customer's bank account with the following features:
- **Attributes**:
  - `custID`: Unique customer ID.
  - `accountNo`: Account number associated with the customer.
  - `balance`: Current account balance.
  - `interest`: Interest rate for the account.
  - `transactions`: A list of transactions performed on the account.
- **Methods**:
  - `get_balance()`: Returns the current account balance.
  - `deposit(amount)`: Deposits the specified amount into the account, updates the balance, and logs the transaction.
  - `withdraw(amount)`: Withdraws the specified amount from the account, updates the balance, and logs the transaction.
  - `showTransactions()`: Displays the list of all transactions for the account.
  - `__str__()`: Returns a string representation of the account details.

### 2. `Transaction`
Represents a transaction performed on an account with the following features:
- **Attributes**:
  - `__time`: The timestamp of the transaction (formatted as "DD-MM-YYYY, HH:MM:SS").
  - `__amount`: The transaction amount (positive for deposits, negative for withdrawals).
- **Methods**:
  - `getTime()`: Returns the transaction timestamp.
  - `getAmount()`: Returns the transaction amount.
  - `__str__()`: Returns a formatted string of the transaction details.

### 3. Main Program
The `main()` function demonstrates the functionality of the banking system:
- Creates an account with initial balance and interest rate.
- Performs deposit and withdrawal transactions.
- Displays the account details, updated balances, and transaction history.

## How to Run
Run the program in a Python environment:
```bash
python3 account_management.py
'''

class Account:
    def __init__(self, custID, accountNo, balance, interest):
        self.custID = custID
        self.accountNo = accountNo
        self.balance = balance
        self.interest = interest
        self.transactions = []
    
    def get_balance(self):
        return self.balance
        
    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            transaction = Transaction(amount)
            self.transactions.append(transaction)
            return self.balance  
        
    def withdraw (self, amount):
        if amount > 0:
            self.balance -= amount
            transaction = Transaction(-amount)
            self.transactions.append(transaction)
            return self.balance
        
    def showTransactions (self):
        for transaction in self.transactions:
            print (transaction)

        
    def __str__(self):
        return (f"Customer ID = {self.custID} \n Account number = {self.accountNo} \n Balance = {self.balance} \n Interest = {self.interest}")

    
class Transaction:
    def __init__(self, amount):
        self.__time = self.__getTimeAsStr()
        self.__amount = amount

    def __getTimeAsStr(self):
        from datetime import datetime
        now = datetime.now() # current date and time
        date_time = now.strftime("%d-%m-%Y, %H:%M:%S")
        return date_time

    def getTime(self):
        return self.__time
 
    def getAmount(self):
        return self.__amount

    def __str__(self):
        return f"Transaction timestamp: {self.__time}, amount: {self.__amount}"
    


def main():
    account1 = Account(1, 1000, 50000, 7)
    print(account1)
    account1.deposit(500)
    print(f'New balance after depositing 500 is {account1.get_balance()}')
    account1.withdraw(1000)
    print(f'New balance after withdrawal of 1000 is {account1.get_balance()}')
    account1.showTransactions()

main ()
