class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if self.unit != other.unit:
            raise ValueError("Нельзя сложить разные меры значения")
        return Weight(self.value + other.value, self.unit)

    def __sub__(self, other):
        if self.unit != other.unit:
            raise ValueError("Нельзя вычитать разные меры значение")
        result = self.value - other.value
        if result < 0:
            raise ValueError("Результат не может быть отрицательным")
        return Weight(result, self.unit)

    def __eq__(self, other):
        return self.value == other.value and self.unit == other.unit

    def __lt__(self, other):
        if self.unit != other.unit:
            if self.unit != other.unit:
                raise ValueError("Нельзя сравнивать разные меры измерения")
        return  self.value < other.value

    def __gt__(self, other):
        if self.unit != other.unit:
            raise ValueError("Нельзя сравнить разные меры измерения")
        return self.value > other.value



