from src.item import Item


class Phone(Item):


    """Phone содержит все атрибуты класса `Item` и дополнительно атрибут,
    содержащий количество поддерживаемых сим - карт"""
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """repr для класса Phone"""
        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.price}, {self.quantity}, {self.number_of_sim})"

    def number_of_sim(self):
        if self.number_of_sim <= 0:
            raise ValueError
        else:
            return self.number_of_sim


phone1 = Phone("iPhone 14", 120_000, 5, 0)

print(phone1.number_of_sim)


