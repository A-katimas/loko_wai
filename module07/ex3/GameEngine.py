from . import CardFactory
from . import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self):
        hand = [
            self.factory.create_creature("daragoun"),
            self.factory.create_creature("gobl1"),
            self.factory.create_spell("Nainja"),
        ]

        self.cards_created += len(hand)

        result = self.strategy.execute_turn(hand, [])

        self.turns += 1
        self.total_damage += result["damage_dealt"]

        return result

    def get_engine_status(self):
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
