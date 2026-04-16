import pytest
from praktikum.ingredient import Ingredient
from tests.test_data import IngredientTypes


class TestIngredientInit:
    
    def test_init_sets_type_correctly(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.type == IngredientTypes.SAUCE
    
    def test_init_sets_name_correctly(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.name == "test"
    
    def test_init_sets_price_correctly(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.price == 100
    
    def test_init_with_novalid_type(self):
        ingredient = Ingredient("NOVALID", "test", 100)
        assert ingredient.type == "NOVALID"
    
    def test_init_with_empty_name_stores_it(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "", 100)
        assert ingredient.name == ""
    
    def test_init_with_zero_price_stores_it(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 0)
        assert ingredient.price == 0
    
    def test_init_with_negative_price_stores_it(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", -50)
        assert ingredient.price == -50
    
    def test_init_with_float_price_stores_it(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 99.99)
        assert ingredient.price == 99.99


class TestIngredientGetType:
    
    def test_get_type_returns_sauce_type(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.get_type() == IngredientTypes.SAUCE
    
    def test_get_type_returns_filling_type(self):
        ingredient = Ingredient(IngredientTypes.FILLING, "test", 100)
        assert ingredient.get_type() == IngredientTypes.FILLING
    
    def test_get_type_returns_invalid_type(self):
        ingredient = Ingredient("INVALID", "test", 100)
        assert ingredient.get_type() == "INVALID"
    
    def test_get_type_returns_same_as_type_attribute(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.get_type() == ingredient.type


class TestIngredientGetName:
    
    def test_get_name_returns_normal_name(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"
    
    def test_get_name_returns_empty_string(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "", 100)
        assert ingredient.get_name() == ""
    
    def test_get_name_returns_name_with_spaces(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "very hot sauce", 100)
        assert ingredient.get_name() == "very hot sauce"
    
    def test_get_name_returns_name_with_numbers(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "sauce123", 100)
        assert ingredient.get_name() == "sauce123"
    
    def test_get_name_returns_long_name(self):
        long_name = "a" * 100
        ingredient = Ingredient(IngredientTypes.SAUCE, long_name, 100)
        assert ingredient.get_name() == long_name
    
    def test_get_name_returns_same_as_name_attribute(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.get_name() == ingredient.name


class TestIngredientGetPrice:

    @pytest.mark.parametrize("price", [
        0,
        100,
        -50,
        99.99,
        1000,
        0.01,
    ])
    def test_get_price_returns_correct_price(self, price):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", price)
        assert ingredient.get_price() == price
    
    def test_get_price_returns_same_as_price_attribute(self):
        ingredient = Ingredient(IngredientTypes.SAUCE, "test", 100)
        assert ingredient.get_price() == ingredient.price
