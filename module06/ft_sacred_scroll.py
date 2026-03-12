import alchemy
from alchemy.potions import healing_potion as heal


def main():

    print("test direct :")
    print(alchemy.elements.create_fire())
    print(alchemy.elements.create_air())
    print(alchemy.elements.create_earth())
    print(alchemy.elements.create_water())

    print("\ntry not direct:")
    try:
        print(alchemy.create_air())
    except AttributeError:
        print("i can't")
    try:
        print(alchemy.create_fire())
    except AttributeError:
        print("i can't")
    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("i can't")
    try:
        print(alchemy.create_water())
    except AttributeError:
        print("i can't")

    print("\n=== import potions ===")
    print(heal())

    print("\nversion : ", alchemy.__version__)
    print("author:", alchemy.__author__)


main()
