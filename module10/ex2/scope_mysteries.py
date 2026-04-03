from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    init_power = initial_power
    accumulation = init_power

    def accumulator(more: int) -> str:
        nonlocal init_power
        nonlocal accumulation
        accumulation += more
        return f"Base {init_power}, add {more}: {accumulation}"

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment_item(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchantment_item


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("mage_counter")
    chieng = mage_counter()
    print(chieng())
    print(chieng())
    print(chieng())
    wouf = mage_counter()
    print(wouf())
    print("=" * 20)
    print("accumulator")
    loug = spell_accumulator(100)
    print(loug(20))
    print(loug(30))
    print("=" * 20)
    print("enchant")
    fire_espect = enchantment_factory("fire_espect")
    print(fire_espect("sword"))
    print(fire_espect("arow"))
    print("=" * 20)
    print("memory")
    memo = memory_vault()
    memo["store"]("chien", 1)
    memo["store"]("wouf", 2)
    print(memo["recall"]("andive"))
    print(memo["recall"]("wouf"))
    print(memo["recall"]("chien"))


if __name__ == "__main__":
    main()
