import alchemy


def main():

    print("=== Sacred Scroll Mastery ===")

    print("Testing direct module access:")
    print(alchemy.elements.create_fire())
    print(alchemy.elements.create_air())
    print(alchemy.elements.create_earth())
    print(alchemy.elements.create_water())

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_air():", end="")
        print(alchemy.create_air())
    except AttributeError:
        print(" AttributeError - not exposed")
    try:
        print("alchemy.create_fire():", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print(" AttributeError - not exposed")
    try:
        print("alchemy.create_earth():", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print(" AttributeError - not exposed")
    try:
        print("alchemy.create_water():", end="")
        print(alchemy.create_water())
    except AttributeError:
        print(" AttributeError - not exposed")

    print("\nPackage metadata:")
    print("version : ", alchemy.__version__)
    print("author:", alchemy.__author__)


main()
