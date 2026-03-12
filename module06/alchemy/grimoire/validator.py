def validate_ingredients(ingredients: str) -> str:
    good_spell = {"fire": 0, "water": 0, "earth": 0, "air": 0}
    try:
        good_spell[ingredients]
        return f"[{ingredients}] - VALID"

    except KeyError:
        return f"[{ingredients}] - INVALID"
