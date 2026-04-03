from typing import Callable, Any
import operator
import functools


def spell_reducer(spells: list[int], operation: str) -> int:
    key = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    try:
        rtr = functools.reduce(lambda x, y: key[operation](x, y), spells)
    except KeyError:
        return 0
    return rtr


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, power=50, element="fire")
    ice = functools.partial(base_enchantment, power=50, element="ice")
    lightning = functools.partial(
        base_enchantment, power=50, element="lightning"
    )

    return {"fire": fire, "ice": ice, "lightning": lightning}


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(unknow: Any) -> str:
        return "i don't know"

    @cast_spell.register
    def cast_spell_int(know: int) -> str:
        return f"spell domage = {know}"

    @cast_spell.register
    def cast_spell_stt(know: str) -> str:
        return f"I cast {know}"

    @cast_spell.register
    def _(arg: list):
        return [cast_spell(x) for x in arg]

    return cast_spell


def fireball(power: int, element: str):
    return f"he said icast , he make {power} domage with {element} element"


def main():
    print("spell_reducer")
    print(spell_reducer([1, 2, 3, 4, 5], "multiply"))
    print("=" * 50)
    print("fibonacii 100")
    print("fibo 10 : ", memoized_fibonacci(10))
    print(memoized_fibonacci.cache_info())
    print("fibo 100 : ", memoized_fibonacci(100))
    print(memoized_fibonacci.cache_info())
    print("fibo 50 : ", memoized_fibonacci(50))
    print(memoized_fibonacci.cache_info())
    print("=" * 50)
    print("spell dispatcher")
    a = spell_dispatcher()
    print(a(12))
    print(a("wouf"))
    print(
        a(
            [
                123,
                "testicular torsion",
                123,
                "skibidi skidoudel now your ___ is a noudel",
            ]
        )
    )
    print(a({"chien": 2}))
    print("=" * 50)
    print("partiel")
    b = partial_enchanter(fireball)
    print(b["fire"](power=2))
    print(b["ice"]())
    print(b["lightning"](power=100))

if __name__ == "__main__":
    main()
