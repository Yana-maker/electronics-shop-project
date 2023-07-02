import pytest
from src.keyboard import KeyBoard

@pytest.fixture
def item():
    item = KeyBoard("1", 2, 3)
    return item

def test_init_lang(item):
    assert item.language == 'EN'

def test_chang_lang(item):
    item.change_lang().change_lang()
    assert item.language == 'EN'

