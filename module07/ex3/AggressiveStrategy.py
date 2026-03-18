# ex3/AggressiveStrategy.py
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = battlefield
        mana_used = 0
        damage = 0

        for card in hand:
            if card.cost <= 3:
                cards_played.append(card.name)
                mana_used += card.cost
                damage += getattr(card, "attack", 2)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets) -> list:
        return available_targets
