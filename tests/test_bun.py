import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name", [
        "black bun",
        "кирилическая булочка", 
        "",
        "123bun",
        "bun!@#$%",
        "a" * 100,
    ])
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name


    @pytest.mark.parametrize("price", [
        0,
        100,
        299.99,
        -100,
    ])
    def test_get_price_return_correct_price(self, price):
        bun = Bun("test bun", price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("", 0),
        ("red bun", 99.99),
        ("", -50),
    ])
    def test_bun_creation_set_attributes_correct(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name_returs_attribute_name(self):
        bun = Bun("test bun", 100)
        assert bun.get_name() == bun.name

    def test_get_price_returs_attribute_price(self):
        bun = Bun("test bun", 100)
        assert bun.get_price() == bun.price
