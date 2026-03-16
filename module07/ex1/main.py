from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import Spellcard
from ex1.Deck import Deck

dragoun = CreatureCard("dragoun", 3, "legendary", 4, 10)
Spell = Spellcard("name", 1, "ma", "pioche")
artifact = ArtifactCard("epée", 3, "Rare", 10, "attaque")

cards = [dragoun, Spell, artifact]
deckmain = Deck(cards)
print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")

print(deckmain.get_deck_stats())
total = deckmain.get_deck_stats()["total cards"]
print("shufle")
deckmain.shuffle()
print("Drawing and playing cards:")
mana = 30

for i in range(0, total):
    card = deckmain.draw_card()
    print("\nDrew: ", card.__class__.__name__)
    print("Play result: ", card.play({"mana": 1}))

print("\nPolymorphism in action: Same interface, different card behaviors!")
