from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        education = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. {education}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        education = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учился с Игорем в группе {self.group}. {education}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}. {education}")


# Примеры
cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()

fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()
print(fr1.age)

