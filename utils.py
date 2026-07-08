def get_number(message):
    while True:
        number = input(message).strip()
        if number.isdigit():
            number = int(number)
            if number > 0:
                return number
            print("❌ Invalid input. Please enter a positive number.")
            continue
        print("❌ Invalid input.Please Insert Only Numbers")


def get_full_name(message):
    while True:
        full_name = input(message).strip().title()
        if len(full_name.split()) < 2:
            print("❌ Please enter your full name.")
            continue
        valid = True
        for word in full_name.split():
            if not word.isalpha():
                valid = False
                break
        if not valid:
            print("❌ Invalid input. Name should contain letters only.")
            continue
        return full_name


def get_national_id(message):
    while True:
        national_id = input(message).strip()
        if national_id.isdigit():
            if len(national_id) == 6:
                return national_id
            print("❌ National ID must be only 6 digits.")
            continue
        print("❌ National ID must contain digits only.")


def get_positive(message):
    while True:
        number = input(message).strip()
        try:
            number = float(number)
            if number > 0:
                return number
            print("❌Please enter a positive number.")
        except ValueError:
            print("❌ Please enter numbers only.")


def get_menu_choice(message):
    while True:
        choices = input(message).strip()
        if choices.isdigit():
            choices = int(choices)
            if 0 <= choices <= 9:
                return choices
            print("❌ Invalid input.")
            continue
        print("❌ Invalid input.Please Insert Only Numbers")
