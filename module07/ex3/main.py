# ex3/main.py
from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===")

    print("Configuring Fantasy Card Game...")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    print("strategy :", strategy.get_strategy_name())
    print("action:", engine.simulate_turn())

    print("\nGame Report:")
    print(engine.get_engine_status())


if __name__ == "__main__":
    main()
