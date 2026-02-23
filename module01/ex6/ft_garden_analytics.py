class GardenManager:

    def __init__(self, name):
        self.garden_list = []
        self.name = name

    class GardenStats:
        @staticmethod
        def count_plants(garden) -> str:
            return f"have  {len(garden.plants)} plant in garden"

        @staticmethod
        def count_by_type(garden) -> str:
            pla = 0
            flower = 0
            prize = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flower += 1
                elif isinstance(plant, Plant):
                    pla += 1
            return (f"Plant: {pla} Flowering Plant: {flower} "
                    f"PrizeFlower: {prize}")

        @staticmethod
        def average_score(garden) -> str:
            score = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            return f"{garden.name} have {score} garden point"

    def add_garden(self, garden) -> None:
        self.garden_list.append(garden)
        print(
            f"the garden : --{garden.name}-- have been add to",
            f"--{self.name}-- manageur",
        )

    def remove_garden(self, garden) -> None:
        print(
            f"the garden : --{garden.name}- have been removed to",
            f"--{self.name}-- manageur",
        )
        self.garden_list.remove(garden)

    def get_global_stats(self) -> None:
        print(f"\n==🌱 {self.name} list 🌱==")
        for garden in self.garden_list:
            print(f"✨{garden.name}✨")
            print(f"🪴 {GardenManager.GardenStats.count_plants(garden)}")
            print(f"  {GardenManager.GardenStats.count_by_type(garden)}")
            print(GardenManager.GardenStats.average_score(garden))
        print("============\n")

    @classmethod
    def create_garden_network(cls, gardens) -> list["GardenManager"]:
        return [cls(garden) for garden in gardens]

    def utils_validate_name(self) -> None:
        GardenManager.GardenStats.count_by_type()


class Garden:
    def __init__(self, name: str, plants: list["Plant"]):
        self.name = name
        self.plants = plants

    def add_plant(self, plant) -> "Plant":
        self.plants.append(plant)
        print(f"{plant.name} have been add to the garden")
        return plant

    def remove_plant(self, plant) -> None:
        self.plants.remove(plant)
        print(f"{plant.name} have been removed")

    def get_stats(self) -> None:
        print(f"\n=== plant in {self.name} ===")
        for plant in self.plants:
            print(f"{plant}")
        print("============\n")
        pass

    def Garden_Helping(self) -> None:
        print("\n==🩹 Garden Help 🩹==")
        print(f"{self.name} helping all plant")
        for plant in self.plants:
            plant.grow()
        print("============\n")


class Plant:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def grow(self) -> str:
        print(f"{self.name} grew 1cm")
        self.age += 1

    def __repr__(self) -> str:
        return f"{self.name}: {self.age}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, age: int, flower_color: str, season: str):
        self.flower_color = flower_color
        self.season = season
        super().__init__(name, age)

    def bloom(self) -> str:
        return f"{self.flower_color} flowers (blooming)"

    def __repr__(self) -> str:
        return super().__repr__() + ", " + self.bloom()


class PrizeFlower(FloweringPlant):
    def __init__(
        self, prize_points: int, name: str, age: int,
        flower_color: str, season: str
    ):
        self.prize_points = prize_points
        super().__init__(name, age, flower_color, season)

    def get_point(self) -> str:
        return f"prize point : {self.prize_points}"

    def __repr__(self) -> str:
        return super().__repr__() + ", " + self.get_point()


def main():

    print(" === Garden Management System Demo === ")
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
        PrizeFlower(500, "sakura", 2, "pink", "sumer"),
    ]
    alice = Garden("alice_garden🌺", jardin_alice)
    ben = Garden("ben_garden🌸", jardin_ben)

    Hello_Garden.add_garden(alice)
    Hello_Garden.add_garden(ben)

    alice.add_plant(Plant("oack", 35))
    alice.Garden_Helping()
    Hello_Garden.get_global_stats()
    alice.remove_plant(jardin_alice[6])
    alice.get_stats()
    ben.get_stats()

    gardens: list[GardenManager] = GardenManager.create_garden_network(
        ["first", "second"]
    )
    gardens[0].add_garden(Garden("robert", jardin_alice))


if __name__ == "__main__":
    main()
