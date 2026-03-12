from alchemy.transmutation import basic
from alchemy.transmutation import advanced
import alchemy.transmutation


print("=== Pathway Debate Mastery ===")

print("Testing Absolute Imports (from basic.py):")
print(basic.lead_to_gold())
print(basic.stone_to_gem())
print(basic.create_earth())
print(basic.create_fire())


print("\nTesting Relative Imports (from advanced.py):")
print(advanced.elixir_of_life())
print(advanced.philosophers_stone())
print(advanced.heal())
print(advanced.lead_to_gold())


print("\nTesting Package Access:")
print(alchemy.transmutation.stone_to_gem())
print(alchemy.transmutation.lead_to_gold())
print(alchemy.transmutation.elixir_of_life())
print(alchemy.transmutation.philosophers_stone())
