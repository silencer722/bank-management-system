class Account:
    next_account_number = 1000

    def __init__(self, owner):
        self.account_number = Account.next_account_number
        Account.next_account_number += 1

        self.owner = owner
        self._balance = 0.0
        self.history = []

    def deposit(self, amount, record_history=True):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return False
        self._balance += amount
        if record_history:
            self.history.append(f"Deposited ${amount:.2f}")
            print(f"✅ ${amount:.2f} deposited successfully.")
        return True

    def withdraw(self, amount, record_history=True):
        if amount <= 0:
            print("❌ Withdraw amount must be positive.")
            return False
        if amount > self._balance:
            print("❌ Insufficient Balance ")
            return False
        self._balance -= amount
        if record_history:
            self.history.append(f"Withdrew ${amount:.2f}")
            print(f"✅ ${amount:.2f} withdrew successfully.")
        return True

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("❌ Transfer amount must be positive.")
            return False
        if amount > self._balance:
            print("❌ Insufficient Balance")
            return False
        if self is other_account:
            print("❌ Sender and receiver accounts cannot be the same.")
            return False
        success = self.withdraw(amount, record_history=False)
        if not success:
            return False
        receiver_success = other_account.deposit(amount, record_history=False)
        if not receiver_success:
            self.deposit(amount, record_history=False)
            return False
        self.history.append(
            f"Transferred ${amount:.2f} to the {other_account.owner.full_name} - {other_account.account_number}"
        )
        other_account.history.append(
            f"Received ${amount:.2f} from {self.owner.full_name} - {self.account_number}"
        )
        print(f"✅ ${amount:.2f} transferred successfully.")
        return True

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "balance": self._balance,
            "history": self.history,
        }

    @classmethod
    def from_dict(cls, data, owner):
        account = cls(owner)

        account.account_number = data["account_number"]
        account._balance = data["balance"]
        account.history = data["history"]

        return account

    def __str__(self):
        return (
            f"Account Number: {self.account_number} | " f"Balance: ${self._balance:.2f}"
        )
