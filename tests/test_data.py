from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientTypes:
    SAUCE = INGREDIENT_TYPE_SAUCE
    FILLING = INGREDIENT_TYPE_FILLING


class BurgerTestData:
    BUNS = {
        "default": ("Test Bun (dont eat!)", 100),
        "first": ("first bun", 100),
        "second": ("second bun", 200),
        "cheap": ("cheap bun", 50),
        "expensive": ("expensive bun", 300),
    }

    INGREDIENTS = {
        "sauce": (IngredientTypes.SAUCE, "Souce emulator", 50),
        "filling": (IngredientTypes.FILLING, "Velociraptor meat", 150),
        "sauce1": (IngredientTypes.SAUCE, "hot sauce", 100),
        "sauce2": (IngredientTypes.SAUCE, "sour cream", 200),
        "filling1": (IngredientTypes.FILLING, "cutlet", 200),
        "filling2": (IngredientTypes.FILLING, "dinosaur", 300),
        "move1": (IngredientTypes.SAUCE, "1", 10),
        "move2": (IngredientTypes.FILLING, "2", 20),
        "move3": (IngredientTypes.SAUCE, "3", 30),
    }

    RECEIPTS = {
        "full": """(==== Test Bun (dont eat!) ====)
= sauce Souce emulator =
= filling Velociraptor meat =
(==== Test Bun (dont eat!) ====)

Price: 400""",
        "bun_only": """(==== Test Bun (dont eat!) ====)
(==== Test Bun (dont eat!) ====)

Price: 200""",
        "one_ingredient": """(==== Test Bun (dont eat!) ====)
= sauce Souce emulator =
(==== Test Bun (dont eat!) ====)

Price: 250"""
    }
