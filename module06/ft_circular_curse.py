from alchemy.grimoire import validator, spellbook

print("=== Circular Curse Breaking ===")

print("\nTesting ingredient validation:")
print(validator.validate_ingredients("fire air"))
print(validator.validate_ingredients("dragon scales"))

print("\nTesting spell recording with validation:")
print(spellbook.record_spell("bdf", "fire"))
print(spellbook.record_spell("squeleton", "bones"))

print("\nTesting late import technique:")
print(spellbook.record_spell("Lightning", "air"))

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
