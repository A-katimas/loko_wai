from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*positions, **noms):
        result1 = spell1(*positions, **noms)
        result2 = spell2(*positions, **noms)
        return (result1, result2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: float) -> Callable:
    def amplified(*args, **kwargs):
        if "power" in kwargs:
            kwargs["power"] *= multiplier
        elif len(args) > 1:
            args = list(args)
            args[1] *= multiplier
            args = tuple(args)
        return base_spell(*args, **kwargs)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def test(*ac, **av):
        if condition(ac[1]):
            return spell(*ac, **av)
        return "Spell fizzled"

    return test


def spell_sequence(spells: list[Callable]) -> Callable:
    def combo(*ac, **av):
        backspell = []
        for spell in spells:
            backspell.append(spell(*ac, **av))
        return backspell

    return combo


def fireball(target):
    return f"Fireball hits {target} 🔥"


def heal(target):
    return f"Heal restores {target} ❤️"


def flash(target):
    return f"Flash blinds {target} ⚡"


def megaflame(target: int, mana: int):
    return f"Fireball hits {target} 🔥 use {mana}"


def mana_check(mana):
    return mana >= 10


def main():
    power = 20
    print("spell_combiner")
    print(spell_combiner(flash, fireball)("dragon"))
    print("spell_sequence")
    print(spell_sequence([fireball, heal, flash])("goblin"))
    print("conditional_caster")
    print(conditional_caster(mana_check, megaflame)("wouf", power))
    print("power_amplifier")
    print(power_amplifier(megaflame, 2)("chien", power))


if __name__ == "__main__":
    main()
