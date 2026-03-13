from ex0 import Card


class Spellcard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        info = game_state
        info.update(
            {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Spell summoned to battlefield",
            }
        )
        game_state["mana"] -= self.cost
        return info

    def resolve_effect(self, targets: list) -> dict:
        return {
            "target": targets,
            "effect": self.effect_type,
        }
