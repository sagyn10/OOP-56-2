class ConstructionTool:
    def __init__(self, name, power_source, weight, material, length, price):
        self.name = name
        self.power_source = power_source
        self.weight = weight
        self.material = material
        self.length = length
        self.price = price

    def use(self):
        print(f"{self.name} используется для строительных работ.")

    def info(self):
        print(f"Инструмент: {self.name}")
        print(f"Источник питания: {self.power_source}")
        print(f"Вес: {self.weight} кг")
        print(f"Материал: {self.material}")
        print(f"Длина: {self.length} см")
        print(f"Цена: {self.price} сом")


class Hammer(ConstructionTool):
    def __init__(self, name, power_source, weight, material, length, price):
        self.name = name
        self.power_source = power_source
        self.weight = weight
        self.material = material
        self.length = length
        self.price = price

    def use(self):
        print(f"{self.name} используется для строительных работ.")

    def info(self):
        print(f"Инструмент: {self.name}")
        print(f"Источник питания: {self.power_source}")
        print(f"Вес: {self.weight} кг")
        print(f"Материал: {self.material}")
        print(f"Длина: {self.length} см")
        print(f"Цена: {self.price} сом")


class Screwdriver(ConstructionTool):
    def __init__(self, name, power_source, weight, material, length, price):
        super().__init__(name, power_source, weight, material, length, price)

    def use(self):
        print(f"{self.name} используется для строительных работ.")

    def info(self):
        print(f"Инструмент: {self.name}")
        print(f"Источник питания: {self.power_source}")
        print(f"Вес: {self.weight} кг")
        print(f"Материал: {self.material}")
        print(f"Длина: {self.length} см")
        print(f"Цена: {self.price} сом")


class Trowel(ConstructionTool):
    def __init__(self, name, power_source, weight, material, length, price):
        super().__init__(name, power_source, weight, material, length, price)

    def use(self):
        print(f"{self.name} используется для строительных работ.")

    def info(self):
        print(f"Инструмент: {self.name}")
        print(f"Источник питания: {self.power_source}")
        print(f"Вес: {self.weight} кг")
        print(f"Материал: {self.material}")
        print(f"Длина: {self.length} см")
        print(f"Цена: {self.price} сом")


# Создаем объекты
hammer = Hammer(name="Молоток", power_source="Ручной", weight="1", material="Сталь", length="25", price="500")
screwdriver = Screwdriver(name="Отвертка", power_source="Ручной", weight="0.3", material="Сталь + Пластик", length="15", price="300")
trowelb = Trowel(name="Мастерок", power_source="Ручной", weight="0.8", material="Сталь + Дерево", length="24", price="350")

hammer.info()
hammer.use()

print()  # Пустая строка для разделения

screwdriver.info()
screwdriver.use()

print()

trowelb.info()
trowelb.use()











