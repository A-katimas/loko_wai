import random


class Game_Even_Generator:
    def __init__(self, player: list[dict], action: dict = {}):
        self.player = player
        self.action = list(action)

    def generate_event(self, nb):
        for i in range(1, nb + 1):
            player = random.choice(self.player)
            level = random.randint(1, 20)
            action = random.choice(self.action)
            yield f"Event {i}: Player {player["name"]} (level {level}) {action}"


class EventAnalyzer:
    def __init__(slef, total: int, hight_lvl: int, tresort: int, lvl_up: int):
        self.total = total
        self.hight_lvl = hight_lvl
        self.tresort = tresort
        self.lvl_up = lvl_up


def main():
    player = [{"name": "alice",
                "lvl": 0
            },
            {
                "name": "ben",
                "lvl": 0
            },
            {
                "name": "aka",
                "lvl": 0
            }
        ]
    action = {"lvl up", "open tresor", "kill mob"}
    lvl = {0, 0, 0}
    Game = Game_Even_Generator(player, action)

    print("=== Game Data Stream Processor ===")

    print("Processing 1000 game events...")
    for event in Game.generate_event(3):
        print(event)

    print("bijour")


if __name__ == "__main__":
    main()
