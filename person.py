class Person:
    def __init__(self, full_name, age, id_national):
        self.full_name = full_name.strip().title()
        self.age = age
        self.id_national = id_national

    def __str__(self):
        return (
            f"{self.full_name} - {self.age} years old - ID Number: {self.id_national}"
        )
