from ex0 import Card
from .ArtifactCard import ArtifactCard
from .SpellCard import Spellcard
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
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card | None:
        if self.deck:
            return self.deck.pop()
        return None

    def get_deck_stats(self) -> dict:
        return {
            "total cards": len([e for e in self.deck if isinstance(e, Card)]),
            "creatures": len(
                [e for e in self.deck if isinstance(e, CreatureCard)]
            ),
            "artifact": len(
                [e for e in self.deck if isinstance(e, ArtifactCard)]
            ),
            "spell": len([e for e in self.deck if isinstance(e, Spellcard)]),
        }
