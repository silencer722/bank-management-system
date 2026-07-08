from person import Person
from account import Account


class Customer(Person):
    def __init__(self, full_name, age, id_national):
        super().__init__(full_name, age, id_national)
        self.accounts = []

    def create_account(self):
        new_account = Account(self)
        self.accounts.append(new_account)
        return new_account

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def close_account(self, account_number):
        account_deleted = self.find_account(account_number)
        if account_deleted:
            if account_deleted._balance == 0:
                self.accounts.remove(account_deleted)
                return True
            return False
        return False

    def show_accounts(self):
        return self.accounts

    def to_dict(self):
        return {
            "accounts": [account.to_dict() for account in self.accounts],
            "full_name": self.full_name,
            "age": self.age,
            "id_national": self.id_national,
        }

    @classmethod
    def from_dict(cls, data):
        customer = cls(data["full_name"], data["age"], data["id_national"])

        for account_data in data["accounts"]:
            account = Account.from_dict(account_data, customer)
            customer.accounts.append(account)

        return customer
