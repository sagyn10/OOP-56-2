from tkinter.font import names


class Hero:
    # конструктор класса
    def __init__(self, name, lvl, hp):
      # атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
#метод класса
    def introduce(self):
       return print(f"привет меня зовут {self.name}")

#объект класса
# kirito = Hero("Kirito", 100, 1000)
# asuna = Hero("Asuna", 10, 100)
# kirito.introduce()
















