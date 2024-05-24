```python
class BankAccount(object):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Balance: {self.balance}"


def main():
    # Create two bank accounts
    account1 = BankAccount(1000)
    account2 = BankAccount(500)

    # Print initial balances
    print("Initial balances:")
    print(account1)
    print(account2)

    # Transfer 200 from account1 to account2
    account1.transfer(200, account2)

    # Print updated balances
    print("\nBalances after transfer:")
    print(account1)
    print(account2)

    # Withdraw 300 from account2
    account2.withdraw(300)

    # Print final balances
    print("\nFinal balances:")
    print(account1)
    print(account2)


if __name__ == "__main__":
    main()
```
