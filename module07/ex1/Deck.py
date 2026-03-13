from ex0 import Card
from . import ArtifactCard, SpellCard
from ex0.CreatureCard import CreatureCard
import random


class Deck:
    def __init__(self, deck: list[Card] | None = None):
        if deck is None:
            self.deck = []
        else:
            self.deck = deck

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        if card_name in self.deck:
            self.deck.remove(card_name)
            return True
        else:
            return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        return self.deck.pop()

    def get_deck_stats(self) -> dict:
        return {
            "total cards": self.deck.count,
            "creatures": len(
                [e for e in self.deck if isinstance(e, CreatureCard)]
            ),
            "artifact": len(
                [e for e in self.deck if isinstance(e, ArtifactCard)]
            ),
            "spell": len([e for e in self.deck if isinstance(e, SpellCard)]),
        }
