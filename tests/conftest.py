import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from tests.test_data import BurgerTestData


@pytest.fixture
def test_bun():
    return Bun(*BurgerTestData.BUNS["default"])

@pytest.fixture
def test_sauce_ingredient():
    return Ingredient(*BurgerTestData.INGREDIENTS["sauce"])

@pytest.fixture
def test_filling():
    return Ingredient(*BurgerTestData.INGREDIENTS["filling"])

@pytest.fixture
def test_burger(test_bun, test_sauce_ingredient, test_filling):
    burger = Burger()
    burger.set_buns(test_bun)
    burger.add_ingredient(test_sauce_ingredient)
    burger.add_ingredient(test_filling)
    return burger

@pytest.fixture
def empty_burger():
    return Burger()
