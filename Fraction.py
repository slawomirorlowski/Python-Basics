class Fraction:
    """[summary]
    """

    def __init__(self, numerator: int = 0, denominator: int = 1):
        self.numerator = numerator
        if denominator == 0:
            raise ValueError("Denominator must be != 0")
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

