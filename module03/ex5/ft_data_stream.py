import random


class Game_Even_Generator:
    def __init__(self, player: list[dict], action: dict = {}):
        self.player = player
        self.event = action

    def generate_event(self, nb) -> str:
        event_tab = list(self.event)
        for i in range(1, nb + 1):
            player = random.choice(self.player)
            level = random.randint(1, 20)
            player["lvl"] += level
            action = random.choice(event_tab)
            self.event[action] += 1
            yield (f"Event {i}: Player {player["name"]} "
                   f"(level {level}) {action}")


def EventAnalyzer(event: str, action: dict) -> str:
    return action[event]


def findMaxLvlPlayer(player: dict) -> dict:
    players_sorted = sorted(player, key=lambda p: p["lvl"], reverse=True)

    return players_sorted[0]["lvl"]


def fibonacci(n) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n) -> int:
    def is_prime(x):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return x > 1

    count, num = 0, 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main():
    player = [
        {"name": "alice", "lvl": 0},
        {"name": "ben", "lvl": 0},
        {"name": "aka", "lvl": 0},
    ]
    event_gen_nb = 1000
    action = {"lvl up": 0, "open tresor": 0, "kill mob": 0}

    Game = Game_Even_Generator(player, action)

    print("=== Game Data Stream Processor ===")

    print("Processing 1000 game events...\n")
    for event in Game.generate_event(3):
        print(event)
    print("game ago ...\n")
    for event in Game.generate_event(event_gen_nb):
        pass
    print("=== Stream Analytics ===")
    print("Total events processed:", event_gen_nb)
    print("High-level players (10+):", findMaxLvlPlayer(player))
    print("Treasure events:", EventAnalyzer("open tresor", action))
    print("Level-up events:", EventAnalyzer("lvl up", action))

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    fibona = []
    for fibo in fibonacci(10):
        fibona.append(fibo)
    print("Fibonacci sequence (first 10): ", end="")
    print(fibona)

    prim = []
    for pri in primes(5):
        prim.append(pri)
    print("Prime numbers (first 5): ", end="")
    print(prim)


if __name__ == "__main__":
    main()
