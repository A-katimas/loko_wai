class GardenManager:

    def __init__(self, name):
        self.garden_list = []
        self.name = name

    class GardenStats:
        @staticmethod
        def count_plants(garden):
            return 1

        @staticmethod
        def count_by_type(garden):
            return 1

        @staticmethod
        def average_score(garden):
            return 1

    def add_garden(self, garden):
        self.garden_list.append(garden)
        print(
            f"the garden : --{garden.name}-- have been add to",
            f"--{self.name}-- manageur",
        )
        return ()

    def remove_garden(self, garden):
        print(
            f"the garden : --{garden.name}- have been removed to",
            f"--{self.name}-- manageur",
        )
        self.garden_list.remove(garden)
        return ()

    def get_global_stats(self):
        print(f"=🌱 {self.name} list 🌱=")
        for garden in self.garden_list:
            print(f"{garden.name}")
        print("==============")
        return ()

    @classmethod
    def create_garden_network(cls):
        return ()

    def utils_validate_name(self):
        GardenManager.GardenStats.count_by_type()
        return ()


class Garden:
    def __init__(self, name: str, plants: list["Plant"]):
        self.name = name
        self.plants = plants

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"{plant.name} have been add to the garden")
        return plant

    def remove_plant(self, plant):
        self.plants.remove(plant)
        print(f"{plant.name} have been removed")

    def get_stats(self):
        print(f"== plant in {self.name} ==")
        for plant in self.plants:
            print(f"{plant}")
        print("==============")
        pass


class Plant:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def grow(self):
        print(f"{self.name} grew 1cm")
        self.age += 1

    def __repr__(self):
        return f"{self.name}: {self.age}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, age: int, flower_color: str, season: str):
        self.flower_color = flower_color
        self.season = season
        super().__init__(name, age)

    def bloom(self):
        return f"{self.flower_color} flowers (blooming)"

    def __repr__(self):
        return super().__repr__() + ", " + self.bloom()


class PrizeFlower(FloweringPlant):
    def __init__(
        self, prize_points: int, name: str, age: int, flower_color: str, season: str
    ):
        self.prize_points = prize_points
        super().__init__(name, age, flower_color, season)

    def get_point(self):
        return f"prize point : {self.prize_points}"

    def __repr__(self):
        return super().__repr__() + ", " + self.get_point()


def main():
    Hello_Garden = GardenManager("Hello_Garden")
    jardin_alice = [
        PrizeFlower(75, "oxalys", 5, "red", "spring"),
        FloweringPlant("rhododendron", 10, "green", "spring"),
        Plant("potatoes", 5),
        FloweringPlant("tomatoes", 10, "yellow", "spring"),
        Plant("soja", 50),
        Plant("spruce", 150),
    ]
    jardin_ben = [
        Plant("fleur", 30),
        FloweringPlant("violette", 20, "purpel", "spring"),
        PrizeFlower("sakura", 2, "pink", "sumer", 500),
    ]
    alice = Garden("alice_garden🌺", jardin_alice)
    ben = Garden("ben_garden🌸", jardin_ben)
    Hello_Garden.add_garden(alice)
    Hello_Garden.add_garden(ben)
    alice.add_plant(Plant("oack", 35))
    Hello_Garden.get_global_stats()
    alice.remove_plant(jardin_alice[1])
    alice.get_stats()
    ben.get_stats()


if __name__ == "__main__":
    main()
