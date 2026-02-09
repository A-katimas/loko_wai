class GardenManager():
    garden_list = [];
    class GardenStats():
        @staticmethod
        def  count_plants(garden):
            return 1;
        @staticmethod
        def count_by_type(garden):
            return 1 ;
        @staticmethod
        def average_score(garden):
            return 1;

    def add_garden(self ,garden):
        return()
    def remove_garden(self ,garden):
        return()
    def get_global_stats(self):
        return()
    @classmethod
    def create_garden_network(cls):
        return()
    def utils_validate_name(self):
        return()

class Garden():
    def __init__(self, name: str, plants: list ["Plant"]):
        self.name = name
        self.plants = plants

    def add_plant(self, plant):
        return(plant)

    def remove_plant(self, plant):
        return(plant)

    def get_stats(self):
        pass

class Plant():
    def __init__(self ,name: str ,age: int):
        self.name = name
        self.age = age

    def grow(self):
        self.age+1;

class FloweringPlant(Plant):
    def __init__(self ,name: str ,age: int ,flower_color: str,
                 season: str):
        self.flower_color = flower_color;
        self.season = season ;
        super().__init__(name, age);

    def bloom(self):
        print("wow")

class PrizeFlower(FloweringPlant):
    def __init__(self, prize_points: int, name: str ,age: int ,flower_color: str , season: str):
        self.prize_points = prize_points;
        super().__init__(name, age,flower_color,season )
    def get_point():
        return 1;

def main():
    rose = PrizeFlower(75, "rose" , 5 , "rose" , "spring")


if __name__ == "__main__" :
    main()