class Plant:
    def __init__(self, name ,height ,age, growsave = 0):
        self.name = name
        self.height= height
        self.age =age
        self.growsave = growsave

    def older(self):
        self.grow();
        self.age += 1;

    def grow(self):
        self.height += 1;
        self.growsave += 1;

    def __repr__(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")

def main():
    rose = Plant("rose", 25, 30)
    print("=== Day 1 ===")
    print(rose);

    for i in range (6):
        rose.older();

    print("=== Day 7 ===")
    print(rose);
    print(f"Growth this week: +{rose.growsave}cm")

if __name__ == "__main__":
    main();