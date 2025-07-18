# class ConstructionTool:
#     def __init__(self, name, power_source, weight, material, length, price):
#         self.name = name
#         self.power_source = power_source
#         self.weight = weight
#         self.material = material
#         self.length = length
#         self.price = price
#
#     def use(self):
#         print(f"{self.name} используется для строительных работ.")
#
#     def info(self):
#         print(f"Инструмент: {self.name}")
#         print(f"Источник питания: {self.power_source}")
#         print(f"Вес: {self.weight} кг")
#         print(f"Материал: {self.material}")
#         print(f"Длина: {self.length} см")
#         print(f"Цена: {self.price} сом")
#
#
# class Hammer(ConstructionTool):
#     def __init__(self, name, power_source, weight, material, length, price):
#         self.name = name
#         self.power_source = power_source
#         self.weight = weight
#         self.material = material
#         self.length = length
#         self.price = price
#
#     def use(self):
#         print(f"{self.name} используется для строительных работ.")
#
#     def info(self):
#         print(f"Инструмент: {self.name}")
#         print(f"Источник питания: {self.power_source}")
#         print(f"Вес: {self.weight} кг")
#         print(f"Материал: {self.material}")
#         print(f"Длина: {self.length} см")
#         print(f"Цена: {self.price} сом")
#
#
# class Screwdriver(ConstructionTool):
#     def __init__(self, name, power_source, weight, material, length, price):
#         super().__init__(name, power_source, weight, material, length, price)
#
#     def use(self):
#         print(f"{self.name} используется для строительных работ.")
#
#     def info(self):
#         print(f"Инструмент: {self.name}")
#         print(f"Источник питания: {self.power_source}")
#         print(f"Вес: {self.weight} кг")
#         print(f"Материал: {self.material}")
#         print(f"Длина: {self.length} см")
#         print(f"Цена: {self.price} сом")
#
#
# class Trowel(ConstructionTool):
#     def __init__(self, name, power_source, weight, material, length, price):
#         super().__init__(name, power_source, weight, material, length, price)
#
#     def use(self):
#         print(f"{self.name} используется для строительных работ.")
#
#     def info(self):
#         print(f"Инструмент: {self.name}")
#         print(f"Источник питания: {self.power_source}")
#         print(f"Вес: {self.weight} кг")
#         print(f"Материал: {self.material}")
#         print(f"Длина: {self.length} см")
#         print(f"Цена: {self.price} сом")
#
#
# # Создаем объекты
# hammer = Hammer(name="Молоток", power_source="Ручной", weight="1", material="Сталь", length="25", price="500")
# screwdriver = Screwdriver(name="Отвертка", power_source="Ручной", weight="0.3", material="Сталь + Пластик", length="15", price="300")
# trowelb = Trowel(name="Мастерок", power_source="Ручной", weight="0.8", material="Сталь + Дерево", length="24", price="350")
#
# hammer.info()
# hammer.use()
#
# print()  # Пустая строка для разделения
#
# screwdriver.info()
# screwdriver.use()
#
# print()
#
# trowelb.info()
# trowelb.use()


# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         if isinstance(new_name, str):
#             self.__name = new_name
#         else:
#             print("Ошибка: имя должно быть строкой")
#
#
# p = Person("Айбек")
# print(p.name)
# p.name = ("Бакыт")
# print(p.name)

from datetime import datetime as dt

def checktime(func):
    def wrapper(*args, **kwargs):
        now = dt.now()
        time_str = now.strftime("%H:%M:%S %d/%m/%Y")
        print(f"Функция была вызвана в {time_str}")
        result = func(*args, **kwargs)  # вызываем саму функцию
        return result

    return wrapper


# Пример использования декоратора
@checktime
def hello_world():
    print("hello world")

# Вызов функции
hello_world()





























