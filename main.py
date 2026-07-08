from bank import Bank
from utils import *
from customer import Customer
from menu import show_menu

bank = Bank()
bank.load()

while True:
    show_menu()
    choice = get_menu_choice("Your option: ")
    if choice == 1:
        full_name = get_full_name("Full Name: ")
        age = get_number("Age: ")
        national_id = get_national_id("National ID: ")
        customer = Customer(full_name, age, national_id)
        existing_customer = bank.find_customer(national_id)
        if existing_customer:
            print("❌ This national ID is already registered.")
            continue
        bank.add_customer(customer)
        print(f"✅ Customer '{customer.full_name}' added successfully.")
    elif choice == 2:
        if bank.customers:
            for customer in bank.show_customers():
                print(customer)
        else:
            print("❌ No customers found.")
    elif choice == 3:
        national_id = get_national_id("National ID: ")
        customer = bank.find_customer(national_id)
        if customer is None:
            print("❌ Customer not found.")
        else:
            account = customer.create_account()
            print(f"✅ Account {account.account_number} created successfully.")
    elif choice == 4:
        national_id = get_national_id("National ID: ")
        customer = bank.find_customer(national_id)
        if customer is None:
            print("❌ Customer not found.")
            continue
        if not customer.accounts:
            print("❌ This customer has no accounts.")
            continue
        for account in customer.accounts:
            print(account)
        account_number = get_number("Account Number: ")
        account = customer.find_account(account_number)
        if account is None:
            print("❌ Account not found.")
            continue
        amount = get_positive("Amount of Deposit: ")
        account.deposit(amount)
    elif choice == 5:
        national_id = get_national_id("National ID: ")
        customer = bank.find_customer(national_id)
        if customer is None:
            print("❌ Customer not found.")
            continue
        if not customer.accounts:
            print("❌ This customer has no accounts.")
            continue
        for account in customer.accounts:
            print(account)
        account_number = get_number("Account Number: ")
        account = customer.find_account(account_number)
        if account is None:
            print("❌ Account not found.")
            continue
        amount = get_positive("Amount of Withdraw: ")
        account.withdraw(amount)
    elif choice == 6:
        national_id_sender = get_national_id("National ID - Sender: ")
        customer_sender = bank.find_customer(national_id_sender)
        if customer_sender is None:
            print("❌ Customer not found.")
            continue
        if not customer_sender.accounts:
            print("❌ This customer has no accounts.")
            continue
        for account in customer_sender.accounts:
            print(account)
        sender_account_number = get_number("Sender Account Number: ")
        sender_account = customer_sender.find_account(sender_account_number)
        if sender_account is None:
            print("❌Sender account not found.")
            continue
        national_id_receiver = get_national_id("National ID - Receiver: ")
        customer_receiver = bank.find_customer(national_id_receiver)
        if customer_receiver is None:
            print("❌ Customer not found.")
            continue
        if not customer_receiver.accounts:
            print("❌ This customer has no accounts.")
            continue
        for account in customer_receiver.accounts:
            print(account)
        receiver_account_number = get_number("Receiver Account Number: ")
        receiver_account = customer_receiver.find_account(receiver_account_number)
        amount = get_positive("Amount of Transfer: ")
        sender_account.transfer(receiver_account, amount)
    elif choice == 7:
        national_id = get_national_id("National ID: ")
        customer = bank.find_customer(national_id)
        if customer is None:
            print("❌ Customer not found.")
            continue
        if not customer.accounts:
            print("❌ This customer has no accounts.")
            continue
        for account in customer.accounts:
            print(account)
    elif choice == 8:
        national_id = get_national_id("National ID: ")
        customer = bank.find_customer(national_id)
        if customer is None:
            print("❌ Customer not found.")
            continue
        if not customer.accounts:
            print("❌ This customer has no accounts.")
            continue
        for account in customer.accounts:
            print(account)
        account_number = get_number("Account Number: ")
        success = customer.close_account(account_number)
        if success:
            print("✅ Account closed successfully.")
        else:
            print(
                "❌ Unable to close the account. Make sure the account exists and its balance is $0.00."
            )
    elif choice == 9:
        national_id = get_national_id("National ID: ")
        customer = bank.find_customer(national_id)
        if customer is None:
            print("❌ Customer not found.")
            continue
        if customer.accounts:
            print("❌ Customer still has active accounts. Close all accounts first.")
            continue
        if bank.remove_customer(customer):
            print(f"✅ Customer '{customer.full_name}' removed successfully.")
    elif choice == 0:
        bank.save()
        print("👋 Thank you for using the Bank Management System.")
        break
