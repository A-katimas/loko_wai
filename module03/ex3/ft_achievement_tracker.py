class Success:
    _call_count = {}

    def __init__(self):
        cls = self.__class__
        self.name = cls.__name__

        if self.name not in Success._call_count:
            Success._call_count[self.name] = 0

        Success._call_count[self.name] += 1

    @classmethod
    def stats(cls) -> dict:
        return cls._call_count


class First_kill(Success):
    pass


class Headshot(Success):
    pass


class lvl_10(Success):
    pass


class speed_demon(Success):
    pass


class Player:
    def __init__(self, name: str):
        self.achievements = set()
        self.name = name

    def add_success(self, success: Success) -> None:
        self.achievements.add(success.name)

    def call_success(self) -> None:
        print(f"Player {self.name} achievements: {self.achievements}")


def main():
    print("=== Achievement Tracker System ===")

    alice = Player("alice")
    ben = Player("ben")
    charlie = Player("charlie")

    ben.add_success(First_kill())
    ben.add_success(speed_demon())

    alice.add_success(First_kill())
    alice.add_success(Headshot())

    charlie.add_success(First_kill())
    charlie.add_success(Headshot())

    players = [alice, ben, charlie]

    # affichage des achievements par joueur
    for p in players:
        p.call_success()
    print("========================\n")
    print("=== Achievement Analytics ===")

    # Tous les achievements uniques
    all_achievements = set()
    for p in players:
        all_achievements |= p.achievements

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print("========================\n")
    # Achievements communs à tous
    common = players[0].achievements.copy()
    for p in players[1:]:
        common &= p.achievements

    print(f"Common to all players: {common}")

    # Achievements rares (1 seul joueur)
    rare = set()
    for ach in all_achievements:
        count = 0
        for p in players:
            if ach in p.achievements:
                count += 1
        if count == 1:
            rare.add(ach)

    print(f"Rare achievements (1 player): {rare}")

    # Comparaison Alice / Ben
    print(f"Alice vs Ben common: {alice.achievements & ben.achievements}")
    print(f"Alice unique: {alice.achievements - ben.achievements}")
    print(f"Ben unique: {ben.achievements - alice.achievements}")

    print("=== Global Call Stats ===")
    print(Success.stats())
    print("========================\n")


# def main():
#     alice = player("alice")
#     ben = player("ben")
#     ben.add_success(First_kill())
#     alice.add_success(First_kill())
#     alice.add_success(Headshot())
#     alice.call_success()
#     ben.call_success()
#     print(Success.stats())


if __name__ == "__main__":
    main()
