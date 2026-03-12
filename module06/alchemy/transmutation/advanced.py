from .basic import lead_to_gold
from ..potions import healing_potion as heal


def philosophers_stone():
    return (
        f"Philosopher’s stone created using {lead_to_gold()} "
        + f" and that thing {heal()}"
    )


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
