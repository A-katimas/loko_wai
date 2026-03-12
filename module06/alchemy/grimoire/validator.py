def validate_ingredients(ingredients: str) -> str:
    good_spell = {"fire": 0, "water": 0, "earth": 0, "air": 0}
    try:
        print(good_spell[ingredients])
        return "[ingredients] - VALID"

    except KeyError:
        return "[ingredients] - INVALID"
