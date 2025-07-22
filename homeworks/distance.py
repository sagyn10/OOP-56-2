class Distance:
    def __init__(self, value, measure):
        self.value = value
        self.measure = measure

    def __str__(self):
        return f"{self.value} {self.measure}"

    def __add__(self, other):
        if self.measure != other.measure:
            raise ValueError("Нельзя сложить разные меры значения")
        return Distance(self.value + other.value, self.measure)

    def __sub__(self, other):
        if self.measure != other.measure:
            raise ValueError("Нельзя вычитать разные меры значение")
        result = self.value - other.value
        if result < 0:
            raise ValueError("Результат не может быть отрицательным")
        return Distance(result, self.measure)

    def __eq__(self, other):
        return self.value == other.value and self.measure == other.measure

    def __lt__(self, other):
        if self.measure != other.measure:
            raise ValueError("Нельзя сравнивать разные меры измерения")
        return self.value < other.value

    def __gt__(self, other):
        if self.measure != other.measure:
            raise ValueError("Нельзя сравнить разные меры измерения")
        return self.value > other.value





