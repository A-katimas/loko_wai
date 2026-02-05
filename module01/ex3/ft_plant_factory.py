class Plant:
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        print(f"Created: {self}")

    def older(self):
        self.grow()
        self.starting_age += 1

    def grow(self):
        self.starting_height += 1

    def __repr__(self):
        return f"{self.name} ({self.starting_height}cm, {self.starting_age}days)"


def main():
    jardin = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]


if __name__ == "__main__":
    main()
