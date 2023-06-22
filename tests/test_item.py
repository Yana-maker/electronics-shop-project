"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

def test_init():
    test = Item("1", 2, 3)
    assert test.name == '1'
    assert test.price == 2
    assert test.quantity == 3

def test_property():
    test = Item("1", 2, 3)
    assert test.name == '1'
    test.name = '3'
    assert test.name == '1'

def test_setter():
    test = Item("1", 2, 3)
    test.name = ('fdsfdsfsdfsd')
    assert test.name == 'fdsfdsfsdf'


def test_calculate_total_price():
    test = Item("1", 2, 3)
    assert test.calculate_total_price() == 6

def test_apply_discount():
    test = Item("1", 2, 3)
    assert test.apply_discount() == 2
    test.pay_rate = 1.5
    assert test.apply_discount() == 3

def test_instantiate_from_csv():
    test = Item("1", 2, 3)
    test.instantiate_from_csv()
    assert len(test.all) == 5


def test_string_to_number():
    test = Item("1", 2, 3)
    assert test.string_to_number('6') == 6
    assert test.string_to_number('5.5') == 5
