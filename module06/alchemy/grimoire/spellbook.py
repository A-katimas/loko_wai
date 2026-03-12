def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator

    return (
        f"Spell recorded: {spell_name} "
        + f" {validator.validate_ingredients(ingredients)}"
    )
