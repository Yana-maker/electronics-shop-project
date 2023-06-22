import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price




    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        # with open(path, newline='') as csvfile:
        with open('../src/items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = cls(row['name'], row['price'], row['quantity'])



    @classmethod
    def string_to_number(cls, value):
        float_value = float(value)
        return int(float_value)


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.isalpha():
            if len(value) <=10:
                self.__name = value
            else:
                self.__name = value[:10]