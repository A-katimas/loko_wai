from .CreatureCard import CreatureCard


def main():
    mana = 10
    dragon = CreatureCard("dragon", 6, "legend", 4, 10)
    knight = CreatureCard("knight", 2, "comon", 2, 5)

    print("=== DataDeck Card Foundation ===")

    print(" \nCreatureCard Info: ")
    print(dragon.get_card_info())
    print(knight.get_card_info())
    print("mana :", mana)

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("playabel :", dragon.is_playable(mana))

    if dragon.is_playable(mana):
        print("play result : ", dragon.play({"mana": mana}))
        mana -= dragon.cost
    print("Fire Dragon attacks knight:")
    print("attack result :", dragon.attack_target(knight))

    print(" \nCreatureCard Info: ")
    print(dragon.get_card_info())
    print(knight.get_card_info())

    print("\nnew test ")
    if dragon.is_playable(mana):
        print("play result : ", dragon.play({"mana": mana}))
        mana -= dragon.cost
    else:
        print(f"Testing insufficient mana ({mana} available):")


main()
