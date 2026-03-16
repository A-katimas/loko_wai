from EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard

mana = 10
dragon = CreatureCard("dragon", 6, "legend", 15, 10)
knight = CreatureCard("knight", 2, "comon", 2, 5)
damonster = EliteCard("the arcane knighté ", 10, "legendary", 20, 10, "physical", 4, 10)

print("=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
print(damonster.get_card_info())
print(dragon.get_card_info())
print("\nPlaying Arcane Warrior (Elite Card):")
print("Combat phase:")
print(damonster.attack(knight))
print(damonster.defend(dragon.attack))


print("\nMagic phase:")
print("spell cast :", damonster.cast_spell("fire ball", [dragon, knight]))
print("mana channel :", damonster.channel_mana(mana))

print("\nMultiple interface implementation successful!")
