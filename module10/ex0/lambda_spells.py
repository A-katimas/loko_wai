def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "*" + x + "*", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(
            sum(map(lambda x: x["power"], mages)) / len(mages), 2
        ),
    }


def main():
    artifacts = [
        {"name": "Water Chalice", "power": 60, "type": "armor"},
        {"name": "Crystal Orb", "power": 82, "type": "accessory"},
        {"name": "Shadow Blade", "power": 98, "type": "relic"},
        {"name": "Storm Crown", "power": 64, "type": "weapon"},
    ]
    mages = [
        {"name": "Luna", "power": 91, "element": "wind"},
        {"name": "Jordan", "power": 69, "element": "wind"},
        {"name": "Phoenix", "power": 65, "element": "fire"},
        {"name": "Rowan", "power": 84, "element": "lightning"},
        {"name": "Morgan", "power": 59, "element": "fire"},
    ]
    spells = ["meteor", "heal", "flash", "blizzard"]

    magestat = mage_stats(mages)

    print("Artifacts triés par puissance :")
    for art in artifact_sorter(artifacts):
        print(art)

    print("=" * 20)
    print("Sorts transformés :")
    for spell in spell_transformer(spells):
        print(spell)

    print("=" * 20)
    print("Stats des mages :")
    print(magestat)

    print("=" * 20)
    print("power filter")
    print(power_filter(mages, 70))


if __name__ == "__main__":
    main()
