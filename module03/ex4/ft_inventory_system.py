import sys

def parse_inventory(args):
    inventory = dict()

    for arg in args:
        if ':' not in arg:
            continue

        name, qty = arg.split(':', 1)
        try:
            qty = int(qty)
        except ValueError:
            continue

        inventory[name] = inventory.get(name, 0) + qty

    return inventory


def main():
    inventory = parse_inventory(sys.argv[1:])

    print("=== Inventory System Analysis ===")

    total_items = 0
    for qty in inventory.values():
        total_items += qty

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("=== Current Inventory ===")

    for name, qty in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
        percent = (qty / total_items) * 100 if total_items > 0 else 0
        print(f"{name}: {qty} units ({percent:.1f}%)")

    print("=== Inventory Statistics ===")

    most_item = None
    least_item = None

    for name, qty in inventory.items():
        if most_item is None or qty > inventory[most_item]:
            most_item = name
        if least_item is None or qty < inventory[least_item]:
            least_item = name

    print(f"Most abundant: {most_item} ({inventory[most_item]} units)")
    print(f"Least abundant: {least_item} ({inventory[least_item]} units)")

    print("=== Item Categories ===")

    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }

    for name, qty in inventory.items():
        if qty >= 6:
            categories["Abundant"].update({name: qty})
        elif qty >= 4:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    for cat, items in categories.items():
        if len(items) > 0:
            print(f"{cat}: {items}")

    print("=== Management Suggestions ===")

    restock = []
    for name, qty in inventory.items():
        if qty <= 1:
            restock.append(name)

    if len(restock) > 0:
        print("Restock needed:", ", ".join(restock))
    else:
        print("Stock levels are healthy")

    print("=== Dictionary Properties Demo ===")

    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in inventory.values()))
    print("Sample lookup - 'sword' in inventory:", inventory.get("sword") is not None)


if __name__ == "__main__":
    main()