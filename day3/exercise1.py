#Exercise 1 - currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        name = self.currency if self.amount == 1 else self.currency + "s"
        return f"{self.amount} {name}"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return Currency(self.currency, self.amount + other.amount)

        if isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)

        return TypeError("Unsupported type")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

        if isinstance(other, (int, float)):
            self.amount += other
            return self

        raise TypeError("Unsupported type")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
print(int(c1))
print(repr(c1))

print(c1 + 5)
print(c1 + c2)

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)