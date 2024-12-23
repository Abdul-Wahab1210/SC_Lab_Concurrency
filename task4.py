import threading
import random
import time

class BankAccount:
    def __init__(self):
        # Initialize balance to 0
        self.balance = 0
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def deposit(self, amount):
        if amount > 0:
            with self.lock:
                self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            with self.lock:
                self.balance -= amount

    def get_balance(self):
        with self.lock:
            return self.balance

class Client(threading.Thread):
    def __init__(self, account):
        super().__init__()
        self.account = account
        self.random = random.Random()

    def run(self):
        for _ in range(10):  # Perform 10 transactions per client
            # Randomly choose deposit or withdraw
            if self.random.choice([True, False]):
                deposit_amount = self.random.randint(1, 100)  # Random deposit between 1 and 100
                self.account.deposit(deposit_amount)
                print(f"{self.name} deposited: {deposit_amount}")
            else:
                withdraw_amount = self.random.randint(1, 100)  # Random withdrawal between 1 and 100
                self.account.withdraw(withdraw_amount)
                print(f"{self.name} withdrew: {withdraw_amount}")

            # Simulate a small delay for realism
            time.sleep(self.random.uniform(0.1, 0.5))  # Random sleep between 0.1 and 0.5 seconds

def main():
    # Create a shared bank account
    account = BankAccount()

    # Create 5 client threads
    clients = [Client(account) for _ in range(5)]

    # Start all threads
    for client in clients:
        client.start()

    # Wait for all threads to finish
    for client in clients:
        client.join()

    # Print the final balance after all transactions
    print(f"Final balance: {account.get_balance()}")

if __name__ == "__main__":
    main()
