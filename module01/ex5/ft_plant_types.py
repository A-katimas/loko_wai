class Plant:
    __instance = []

    def __init__(self, name, starting_height, starting_age):
        self.set_name(name)
        self.set_height(int(starting_height))
        self.set_age(int(starting_age))
        Plant.__instance.append(self)
        print(f"{self}")

    def older(self) -> None:
        self.grow()
        self.set_age(int(self.age) + int(1))

    def grow(self) -> None:
        self.set_height(int(self.height) + int(1))

    def set_height(self, new_height) -> None:
        self.height = new_height

    def set_age(self, new_age) -> None:
        self.age = new_age

    def set_name(self, name) -> None:
        self.name = name

    @classmethod
    def print_instance(cls) -> None:
        for plant in Plant.__instance:
            t = "".join(list(reversed(plant.__class__.__name__))).capitalize()
            print(f"Current {t}:", plant.name,
                  f"({plant.height}cm, {plant.age} days)")
        print("\n")


class Flower(Plant):
    __instance_flower = []

    def __init__(self, name, starting_height, starting_age, color):
        self.color = color
        super().__init__(name, starting_height, starting_age)
        Flower.__instance_flower.append(self)

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    @classmethod
    def print_instance(cls) -> None:
        for flower in cls.__instance_flower:
            print(
                f"Current {flower.__class__.__name__}:",
                flower.name,
                f"({flower.height}cm, {flower.age} days)",
            )
        print("\n")

    def __repr__(self) -> str:
        return (
            f"{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    __instance_tree = []

    def __init__(self, name, starting_height, starting_age, trunk_diameter):
        self.diameter = trunk_diameter
        super().__init__(name, starting_height, starting_age)
        Tree.__instance_tree.append(self)

    def produce_shade(self) -> str:
        return (
            f"{self.name} provides {(self.diameter ** 2)*0.0312}"
            "square meters of shade"
        )

    @classmethod
    def print_instance(cls) -> None:
        for tree in cls.__instance_tree:
            print(
                f"Current {tree.__class__.__name__}:", tree.name,
                f"({tree.height}cm, {tree.age} days)",
            )
        print("\n")

    def __repr__(self) -> str:
        return (
            f"{self.name} (Tree): {self.height}cm, {self.age} days,"
            f"{self.diameter}cm diameter"
        )


class Vegetable(Plant):
    __instance_Vegetable = []

    def __init__(self, name, starting_height, starting_age,
                 harvest_season, nutritional_value):
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, starting_height, starting_age)
        Vegetable.__instance_Vegetable.append(self)

    def boast(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"

    @classmethod
    def print_instance(cls) -> None:
        for vegetable in cls.__instance_Vegetable:
            print(
                f"Current {vegetable.__class__.__name__}:",
                vegetable.name,
                f"({vegetable.height}cm, {vegetable.age} days)",
            )
        print("\n")

    def __repr__(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
            f" {self.harvest_season} harvest"
        )


def main():
    print("=== Garden Plant Types ===")
    jardin = [
        Flower("Rose", 44, 5, "red"),
        Tree("oak", 500, 200, 50),
        Vegetable("tomato", 80, 90, "summer", "vitamine_c"),
    ]
    print("\n")
    print(jardin[0].bloom())
    print(jardin[1].produce_shade())
    print(jardin[2].boast())
    print("\n")
    Plant.print_instance()
    Flower.print_instance()
    Tree.print_instance()
    Vegetable.print_instance()


if __name__ == "__main__":
    main()
