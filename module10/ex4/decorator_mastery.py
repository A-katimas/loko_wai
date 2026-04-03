from typing import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def spendtime(*ac, **ad):
        starttime = time.time()
        result = func(*ac, **ad)
        finaltime = time.time() - starttime
        print(f"Spell completed in {finaltime:.10f} seconds")
        return result

    return spendtime


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*ac, **ad):
            power = ad["power"]
            if power >= min_power:
                return func(*ac, **ad)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*ac, **ad):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*ac, **ad)
                except Exception:
                    if i < max_attempts:
                        print(
                            f"Spell failed, retrying... ({i}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after {max_attempts}",
                            " attempts",
                        )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(e.isalpha() or e.isspace() for e in name)

    @power_validator(10)
    @spell_timer
    @retry_spell(5)
    def cast_spell(self, spell_name: str, power: int = 0) -> str:
        if spell_name == "broken":
            raise ValueError
        return f"cast {spell_name} make {power} domage"


def main():
    mage = MageGuild()
    print("Testing spell timer...")
    print("Casting fireball...")
    print(mage.validate_mage_name("bob"))
    print(mage.validate_mage_name(" z"))
    print(mage.validate_mage_name("tencarvile"))
    print("=" * 10)
    print("wouf")
    print(mage.cast_spell("wouf", power=100000000000000))
    print("giga")
    print(mage.cast_spell("giga fireball", power=10))
    print("raise")
    print(mage.cast_spell("broken", power=20))


if __name__ == "__main__":
    main()
