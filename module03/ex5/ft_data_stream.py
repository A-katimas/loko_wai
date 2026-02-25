import random


class Game_Even_Generator:
    def __init__(self, player: list[dict], action: dict = {}):
        self.player = player
        self.event = action

    def generate_event(self, nb):
        event_tab= list(self.event)
        for i in range(1, nb + 1):
            player = random.choice(self.player)
            level = random.randint(1, 20)
            player["lvl"] += level
            action = random.choice(event_tab)
            self.event[action] += 1
            yield f"Event {i}: Player {player["name"]} (level {level}) {action}"


def EventAnalyzer(event: str, action: dict):
    print("la", action[event])


def main():
    player = [
        {"name": "alice", "lvl": 0},
        {"name": "ben", "lvl": 0},
        {"name": "aka", "lvl": 0},
    ]
    action = {"lvl up": 0, "open tresor": 0, "kill mob": 0}

    Game = Game_Even_Generator(player, action)

    print("=== Game Data Stream Processor ===")

    print("Processing 1000 game events...")
    for event in Game.generate_event(3):
        print(event)
    print("game ago ...")
    for event in Game.generate_event(1000):
        pass
    EventAnalyzer("lvl up", action)
    print(player[2])
    print(action)
    print("bijour")


if __name__ == "__main__":
    main()
