class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        print(f"Created: {self}")

    def older(self) -> None:
        self.grow()
        self.starting_age += 1

    def grow(self) -> None:
        self.starting_height += 1

    def __repr__(self) -> str:
        return (
            f"{self.name} "
            f"({self.starting_height}cm, {self.starting_age}days)"
        )


def main():
    jardin = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    jardin[0].grow()


if __name__ == "__main__":
    main()
