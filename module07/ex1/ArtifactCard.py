from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        info = game_state
        info.update(
            {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Artifact summoned to battlefield",
            }
        )
        game_state["mana"] -= self.cost
        return info

    def activate_ability(self) -> dict:
        return {"durability": self.durability, "effect": self.effect}
