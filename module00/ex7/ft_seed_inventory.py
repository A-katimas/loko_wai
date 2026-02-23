def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    table = {
        "packets": f"{quantity} packets available",
        "grams": f"{quantity} grams total",
        "area": f"covers {quantity} square meters",
    }

    if unit in table:
        print(seed_type.capitalize(), "seeds :", table[unit])

    else:
        print("Unknown unit type")


ft_seed_inventory(input(), int(input()), input())
