# ex3/FantasyCardFactory.py
import random
from .CardFactory import CardFactory, Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import Spellcard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: int | str) -> Card:
        if isinstance(name_or_power, int):
            return CreatureCard("Dragon", name_or_power, "Legendary", 7, 5)
        else:
            return CreatureCard(name_or_power, 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power: int | str):
        if isinstance(name_or_power, int):
            return Spellcard("Fireball", name_or_power, "Rare", "deal damage")
        else:
            return Spellcard(name_or_power, 3, "Rare", "deal damage")

    def create_artifact(self, name_or_power: int | str):
        if isinstance(name_or_power, int):
            return ArtifactCard(
                "Mana Ring", name_or_power, "Common", "gain mana"
            )
        else:
            return ArtifactCard(name_or_power, 2, "Common", "gain mana")

    def create_themed_deck(self, size: int):
        deck = []
        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            if choice == "creature":
                deck.append(self.create_creature(1))
            elif choice == "spell":
                deck.append(self.create_spell("cacaboudin"))
            else:
                deck.append(self.create_artifact("Chien"))
        return {"deck": deck}

    def get_supported_types(self):
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
