class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.Height = height
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.Height}cm, {self.age} days old"


def main():
    a = Plant("rose", 25, 30)
    b = Plant("Sunflower", 80, 45)
    c = Plant("Cactus", 15, 120)

    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()
