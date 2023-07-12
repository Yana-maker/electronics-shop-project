from src.item import Item

class MixinLang:

    __language = 'EN'
    def __init__(self):
        self.__language = MixinLang.__language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
            return self
        elif self.language == "RU":
            self.__language = "EN"
            return self


class KeyBoard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)








