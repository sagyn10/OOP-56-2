class Person:
    def __init__(self, name, birth_date, occupation, higher_education ):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


    def introduce(self):
        print(f"Привет меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(
              f"Привет, меня зовут {self.name}, я одноклассник Игоря, "
              f"учились вместе в {self.group_name}, я родился {self.birth_date}, "
              f"работаю {self.occupation}"
        )

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, я друг Игоря, "
            f"я родился {self.birth_date}, работаю {self.occupation}, "
            f"люблю заниматься: {self.hobby}"
        )



# создаем объекты:
friend1 = Friend(name="Алмаз", birth_date="5.12.2000", occupation="Программист", higher_education=True, hobby="плавание" )
friend2 = Friend(name="Акылай", birth_date="1.03.2001", occupation="Дизайнер", higher_education=True, hobby="рисование")

classmate1 = Classmate(name="Бектур", birth_date="5.12.2000", occupation="Программист", higher_education=True, group_name="11 Д")
classmate2 = Classmate(name="Бакыт", birth_date="12.05.1999", occupation="Инженер", higher_education=True, group_name="11 Д")

# вызываем introduce() у всех:
people = [friend1, friend2, classmate1, classmate2]

for person in people:
    person.introduce()