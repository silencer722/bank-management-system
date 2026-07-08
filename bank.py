import json
from account import Account
from customer import Customer


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        return True

    def find_customer(self, id_national):
        for customer in self.customers:
            if customer.id_national == id_national:
                return customer
        return None

    def remove_customer(self, customer):
        customer_deleted = self.find_customer(customer.id_national)
        if customer_deleted:
            self.customers.remove(customer)
            return True
        return False

    def show_customers(self):
        return self.customers

    def save(self):
        data = [customer.to_dict() for customer in self.customers]

        with open("bank_data.json", "w") as file:
            json.dump(data, file, indent=4)

        return True

    def load(self):
        try:
            with open("bank_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return False

        self.customers.clear()

        max_account_number = 1000

        for customer_data in data:
            customer = Customer.from_dict(customer_data)
            self.customers.append(customer)

            for account in customer.accounts:
                if account.account_number > max_account_number:
                    max_account_number = account.account_number

        Account.next_account_number = max_account_number + 1

        return True
