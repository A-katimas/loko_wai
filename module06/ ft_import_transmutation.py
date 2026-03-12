import alchemy.elements
import alchemy.potions
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water


def main():

    print("=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {create_fire()}")

    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print("\nMethod 3 - Aliased import:")
    print("heal(): ", heal())

    print("\nMethod 4 - Multiple imports:")
    print("create_earth(): ", alchemy.elements.create_earth())
    print("create_fire(): ", alchemy.elements.create_air())
    print("strength_potion(): ", alchemy.potions.strength_potion())

    print("\nAll import transmutation methods mastered!")


main()
