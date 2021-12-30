class Fraction:
    """[summary]
    """

    @staticmethod
    def one():
        return Fraction(1, 1)

    @property
    def numerator(self) -> float:
        return self._numerator

    @property
    def denumerator(self) -> float:
        return self._denominator

    def __init__(self, numerator: int = 0, denominator: int = 1):
        self._numerator = numerator
        if denominator == 0:
            raise ValueError("Denominator must be != 0")
        self._denominator = denominator

    def __str__(self):
        return str(self._numerator) + "/" + str(self._denominator)

    def __float__(self):
        return self._numerator / self._denominator


v = Fraction(1, 2)
v._numerator = 10
print(v)

