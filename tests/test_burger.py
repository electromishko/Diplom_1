import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.test_data import IngredientTypes, BurgerTestData


class TestBurgerInit:
    def test_new_burger_has_no_bun(self, empty_burger):
        assert empty_burger.bun is None

    def test_new_burger_has_empty_ingredients_list(self, empty_burger):
        assert empty_burger.ingredients == []


class TestBurgerSetBuns:
    def test_set_buns_sets_bun_correctly(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)
        assert empty_burger.bun == test_bun

    def test_set_buns_overwrites_previous_bun(self, empty_burger, test_bun, another_test_bun):
        empty_burger.set_buns(test_bun)
        empty_burger.set_buns(another_test_bun)
        
        assert empty_burger.bun == another_test_bun


class TestBurgerAddIngredient:
    def test_add_ingredient_increases_list_length(self, empty_burger, test_sauce_ingredient):
        empty_burger.add_ingredient(test_sauce_ingredient)
        assert len(empty_burger.ingredients) == 1

    def test_add_ingredient_adds_correct_item(self, empty_burger, test_sauce_ingredient):
        empty_burger.add_ingredient(test_sauce_ingredient)
        assert empty_burger.ingredients[0] == test_sauce_ingredient

    def test_add_multiple_ingredients_maintains_order(self, empty_burger, test_sauce_ingredient, test_filling):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)
        
        assert empty_burger.ingredients == [test_sauce_ingredient, test_filling]


class TestBurgerRemoveIngredient:
    def test_remove_ingredient_decreases_list_length(self, empty_burger, test_sauce_ingredient):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.remove_ingredient(0)
        assert len(empty_burger.ingredients) == 0

    def test_remove_ingredient_removes_correct_item(self, empty_burger, test_sauce_ingredient, test_filling):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)
        
        empty_burger.remove_ingredient(0)
        
        assert empty_burger.ingredients == [test_filling]

    def test_remove_ingredient_at_end_removes_last_item(self, empty_burger, test_sauce_ingredient, test_filling):
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)
        
        empty_burger.remove_ingredient(1)
        
        assert empty_burger.ingredients == [test_sauce_ingredient]


class TestBurgerMoveIngredient:
    def test_move_ingredient_order_forward(self, empty_burger, move_ingredient_1, move_ingredient_2):
        empty_burger.add_ingredient(move_ingredient_1)
        empty_burger.add_ingredient(move_ingredient_2)
        
        empty_burger.move_ingredient(0, 1)
        
        assert empty_burger.ingredients == [move_ingredient_2, move_ingredient_1]

    def test_move_ingredient_order_back(self, empty_burger, move_ingredient_1, move_ingredient_2):
        empty_burger.add_ingredient(move_ingredient_1)
        empty_burger.add_ingredient(move_ingredient_2)
        
        empty_burger.move_ingredient(1, 0)
        
        assert empty_burger.ingredients == [move_ingredient_2, move_ingredient_1]

    def test_move_ingredient_to_same_position_no_changes(self, empty_burger, move_ingredient_1, move_ingredient_2):
        empty_burger.add_ingredient(move_ingredient_1)
        empty_burger.add_ingredient(move_ingredient_2)
        
        empty_burger.move_ingredient(0, 0)
        
        assert empty_burger.ingredients == [move_ingredient_1, move_ingredient_2]


class TestBurgerGetPrice:
    def test_get_price_with_bun_only_returns_double_bun_price(self, empty_burger, test_bun):
        empty_burger.set_buns(test_bun)
        
        expected = test_bun.get_price() * 2
        assert empty_burger.get_price() == expected

    def test_get_price_with_bun_and_ingredients_returns_sum(self, empty_burger, test_bun, test_sauce_ingredient):
        empty_burger.set_buns(test_bun)
        empty_burger.add_ingredient(test_sauce_ingredient)
        
        expected = test_bun.get_price() * 2 + test_sauce_ingredient.get_price()
        assert empty_burger.get_price() == expected

    def test_get_price_with_multiple_ingredients_returns_sum_of_all(self, empty_burger, test_bun, test_sauce_ingredient, test_filling):
        empty_burger.set_buns(test_bun)
        empty_burger.add_ingredient(test_sauce_ingredient)
        empty_burger.add_ingredient(test_filling)
        
        expected = test_bun.get_price() * 2 + test_sauce_ingredient.get_price() + test_filling.get_price()
        assert empty_burger.get_price() == expected


class TestBurgerGetReceipt:
    def test_get_receipt_contains_bun_name(self, test_burger):
        receipt = test_burger.get_receipt()
        expected_bun_name = test_burger.bun.get_name()
        
        assert expected_bun_name in receipt
    
    def test_get_receipt_contains_bun_twice(self, test_burger):
        receipt = test_burger.get_receipt()
        expected_bun_name = test_burger.bun.get_name()
        
        assert receipt.count(expected_bun_name) == 2
    
    def test_get_receipt_contains_ingredient_names(self, test_burger):
        receipt = test_burger.get_receipt()
        
        for ingredient in test_burger.ingredients:
            assert ingredient.get_name() in receipt
    
    def test_get_receipt_contains_ingredient_types_lowercase(self, test_burger):
        receipt = test_burger.get_receipt()
        
        for ingredient in test_burger.ingredients:
            assert ingredient.get_type().lower() in receipt
    
    def test_get_receipt_contains_price(self, test_burger):
        receipt = test_burger.get_receipt()
        expected_price = str(test_burger.get_price())
        
        assert expected_price in receipt
    
    def test_get_receipt_format_matches_expected(self, test_burger):
        expected = BurgerTestData.RECEIPTS["full"]
        assert test_burger.get_receipt() == expected


class TestBurgerWithoutBun:
    def test_get_price_without_bun_raises_attribute_error(self, empty_burger):
        with pytest.raises(AttributeError):
            empty_burger.get_price()
    
    def test_get_receipt_without_bun_raises_attribute_error(self, empty_burger):
        with pytest.raises(AttributeError):
            empty_burger.get_receipt()
