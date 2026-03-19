from . import TournamentCard
from . import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 4)

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    print(f"Fire Dragon (ID: {id1}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}\n")

    print(f"Ice Wizard (ID: {id2}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}\n")

    print("Creating tournament match...")
    result = platform.create_match(id1, id2)
    print(f"Match result:{result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()

    for i, card in enumerate(leaderboard, 1):
        print(
            f"{i}. {card.name} - Rating: {card.rating}",
            f" ({card.wins}-{card.losses})",
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
