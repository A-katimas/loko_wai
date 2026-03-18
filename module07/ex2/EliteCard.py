from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        health: int,
        dega: int,
        comba_type: str,
        chaneling: int,
        mana: int,
    ):
        self.dega = dega
        self.comba_type = comba_type
        self.health = health
        self.chaneling = chaneling
        self.mana = mana
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        info = game_state
        info.update(
            {
                "card_played": self.name,
                "mana_used": self.cost,
                "rarity": self.rarity,
                "effect": "Artifact summoned to battlefield",
            }
        )
        game_state["mana"] -= self.cost
        return info

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "type": self.comba_type,
                "attack": self.dega,
                "health": self.health,
                "chaneling": self.chaneling,
            }
        )
        return info

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "dommage": self.dega,
            "combat_type": self.comba_type,
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        alive = True
        if self.health <= 0:
            alive = False
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.health,
            "still_alive": alive,
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack, "health": self.health}

    def channel_mana(self, amount: int) -> dict:
        return {"amount": amount, "mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"chaneling": self.chaneling}

    def cast_spell(self, spell_name: str, targets: list[Card]) -> dict:
        self.mana = int(self.mana / 2)
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [e.name for e in targets],
            "mana_used": int(self.mana / 2),
        }
