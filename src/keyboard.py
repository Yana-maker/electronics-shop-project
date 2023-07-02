from src.item import Item

class MixinLang(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def check_lang(self):
        self._language = 'RU'
        self._language = 'EN'

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"
        return self


class KeyBoard(MixinLang):
    pass



