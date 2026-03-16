from . import Combatable ,Card ,Magical

class EliteCard (Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,dega :int ,comba_type:str):
        self.dega = dega
        self.comba_type = comba_type
        super().__init__(name, cost, rarity)
    def play(self, game_state: dict) -> dict:
        info = game_state
        info.update( {"card_played": self.name,
                    "mana_used": self.cost,
                    "rarity": self.rarity,
                    "effect": "Artifact summoned to battlefield",
                    }
                )
        game_state["mana"] -= self.cost
        return info

    def attack(self, target) -> dict:
        return{
            "attacker" : self.name,
            "target" : target.name,
            "domage" : self.attack,
            "combat_type" : self.comba_type
        }

    def defend(self, incoming_damage: int) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict



    Combat phase:
Attack result: {'attacker': 'Arcane Warrior', 'target': 'Enemy',
'damage': 5, 'combat_type': 'melee'}
Defense result: {'defender': 'Arcane Warrior', 'damage_taken': 2,
'damage_blocked': 3, 'still_alive': True}