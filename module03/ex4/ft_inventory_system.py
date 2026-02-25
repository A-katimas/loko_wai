import sys

# --- Class Item ---
class Item:
    list_item = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Item.list_item[self.name] = Item.list_item.get(self.name, 0) + number

    @classmethod
    def sort_item(cls):
        sorted_items = sorted(cls.list_item.items(), key=lambda x: x[1], reverse=True)
        return sorted_items

# --- Class Inventory ---
class Inventory:
    def __init__(self, items : int):
        self.items = items

    def total_items(self):
        return sum(item.number for item in self.items)

    def unique_item_types(self):
        return len(self.items)

# --- fonction parcing ---
def parse_inventory(args :str):
    inventory = []
    for arg in args:
        if ":" not in arg:
            continue
        name, qty = arg.split(":", 1)
        try:
            qty = int(qty)
        except ValueError:
            continue
        inventory.append(Item(name, qty))
    return inventory

# --- Fonction main ---
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <item1:qty> <item2:qty> ...")
        sys.exit(1)

    items = parse_inventory(sys.argv[1:])
    inventory = Inventory(items)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {inventory.total_items()}")
    print(f"Unique item types: {inventory.unique_item_types()}")

    print("=== Current Inventory ===")
    for name, qty in Item.sort_item():
        percent = (qty / inventory.total_items()) * 100 if inventory.total_items() > 0 else 0
        print(f"{name}: {qty} units ({percent:.1f}%)")

    print("=== Inventory Statistics ===")
    sorted_items = Item.sort_item()
    most_item, least_item = sorted_items[0], sorted_items[-1]
    print(f"Most abundant: {most_item[0]} ({most_item[1]} units)")
    print(f"Least abundant: {least_item[0]} ({least_item[1]} units)")

    print("=== Item Categories ===")
    categories = {"Abundant": {}, "Moderate": {}, "Scarce": {}}
    for name, qty in sorted_items:
        if qty >= 6:
            categories["Abundant"][name] = qty
        elif qty >= 4:
            categories["Moderate"][name] = qty
        else:
            categories["Scarce"][name] = qty
    for cat, items in categories.items():
        if items:
            print(f"{cat}: {items}")

    print("=== Management Suggestions ===")
    restock = [name for name, qty in sorted_items if qty <= 1]
    if restock:
        print("Restock needed:", ", ".join(restock))
    else:
        print("Stock levels are healthy")

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", ", ".join(Item.list_item.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in Item.list_item.values()))
    print("Sample lookup - 'sword' in inventory:", "sword" in Item.list_item)

if __name__ == "__main__":
    main()