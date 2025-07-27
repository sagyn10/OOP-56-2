class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я родился {self.birth_date},  работаю {self.occupation}")

p1 = Person(name="Акыл", birth_date="01.05.2000 году", occupation="Сварщиком", higher_education=False)
p2 = Person(name="Фарид", birth_date="02.03.2001 году", occupation="Пожарным", higher_education=False)

p1.introduce()
p2.introduce()