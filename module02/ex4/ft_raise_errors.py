class Plant:
    def __init__(self, name: str, water: int, sunlight: int):
        self.name = name
        self.water = water
        self.sunlight = sunlight


def check_plant_health(plant_name, water_level, sunlight_hours):

    check_plant(plant_name)
    check_water(water_level)
    check_sunlight(sunlight_hours)

    print(f"✅ Plant {plant_name} is healthy! ✅")
    pass


class Garden_Error(Exception):
    def __init__(self, message: str = " garden"):
        super().__init__(message)


class Plant_Error(Garden_Error):
    def __init__(self):
        super().__init__(" Plant name cannot be empty!🔴")


class Water_Error(Garden_Error):
    def __init__(self, water):
        super().__init__(f" Water level {water} is too high (max 10)🔴")


class Max_Sunlinght_Error(Garden_Error):
    def __init__(self, time: int):
        super().__init__(f" Sunlight hours {time} is too max (max 12)🔴")


class Min_Sunlinght_Error(Garden_Error):
    def __init__(self, time: int):
        super().__init__(f" Sunlight hours {time} is too low (min 2)🔴")


def check_sunlight(sunlight):
    if 2 > sunlight:
        raise Min_Sunlinght_Error(sunlight)
    if 12 < sunlight:
        raise Max_Sunlinght_Error(sunlight)


def check_water(water: int):
    if water > 10:
        raise Water_Error(water)


def check_plant(plant):
    if not isinstance(plant, str) or plant.strip() == "":
        raise Plant_Error()


def main():
    print("=== Garden Plant Health Checker ===\n")
    jardin = [
        Plant("arbre", 5, 13),
        Plant("tomate", 50, 5),
        Plant("chien", 4, 1),
        Plant("plant", 50, 1),
        Plant(name=None, water=3, sunlight=4),
        Plant("Potatoes", 3, 4),
    ]

    try:
        try:
            print("Checking (nothing)...")
            check_plant_health(plant_name=None, water_level=4,
                               sunlight_hours=4)
        except Garden_Error as e:
            print("\033[31mError\033[0m:", e)
            print("Next plant ➡️\n")
        finally:
            for plant in jardin:
                print(f"Checking {plant.name}...")
                try:
                    check_plant_health(plant.name, plant.water, plant.sunlight)
                except Garden_Error as e:
                    print("\033[31mError\033[0m:", e)
                print("Next plant ➡️\n")
    finally:
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
