class Garden_Error(Exception):
    def __init__(self, message: str = " garden"):
        super().__init__(f"{message}")


class Plant_Error(Garden_Error):
    def __init__(self, plant):
        super().__init__(f"Plant name invalid: {plant!r} 🔴")


class Water_Error(Garden_Error):
    def __init__(self, water):
        super().__init__(f"Water level {water} is too high (max 10) 🔴")


class Max_Sunlight_Error(Garden_Error):
    def __init__(self, time):
        super().__init__(f"Sunlight hours {time} is too high (max 12) 🔴")


class Min_Sunlight_Error(Garden_Error):
    def __init__(self, time):
        super().__init__(f"Sunlight hours {time} is too low (min 2) 🔴")


class Water_Tank_Error(Garden_Error):
    def __init__(self):
        super().__init__("Not enough water in tank 🔴")


class Plant:
    def __init__(self, name: str, water: int, sunlight: int):
        self.name = name
        self.water = water
        self.sunlight = sunlight


# Helper functions
def check_plant(plant):
    if not isinstance(plant, str) or plant.strip() == "":
        raise Plant_Error(plant)


def check_water(water):
    if water > 10:
        raise Water_Error(water)


def check_sunlight(sunlight):
    if sunlight < 2:
        raise Min_Sunlight_Error(sunlight)
    if sunlight > 12:
        raise Max_Sunlight_Error(sunlight)


def check_water_tank(water_tank):
    if water_tank < 1:
        raise Water_Tank_Error()


def check_plant_health(plant_name, water_level, sunlight_hours):
    check_plant(plant_name)
    check_water(water_level)
    check_sunlight(sunlight_hours)
    print(f"✅ Plant {plant_name} is healthy! ✅")


# GardenManager class
class GardenManager:
    def __init__(self, lvl_water):
        self.plants = []
        self.lvl_water = lvl_water

    def add_plant(self, name, water, sunlight):
        try:
            check_plant(name)
            check_water(water)
            check_sunlight(sunlight)
            plant = Plant(name, water, sunlight)
            self.plants.append(plant)
            print(f"Added {name} successfully 🌿")
        except Garden_Error as e:
            print(f"\033[31mError\033[0m adding plant: {e}")

    def add_lst(self, plants: [Plant]):
        for plant in plants:
            self.add_plant(plant.name, plant.water, plant.sunlight)

    def water_plants(self):
        print("\nOpening watering system 💧")
        try:
            for plant in self.plants:
                try:
                    check_water_tank(self.lvl_water)
                    try:
                        check_water(plant.water)
                        print(f"Watering {plant.name} - success 🌱")
                    except Water_Error as e:
                        print("\033[31mError\033[0m : "
                              f"watering {plant.name}: {e}")
                    self.lvl_water -= 1
                    plant.water += 1
                except Water_Tank_Error as e:
                    print(f"Error Water Tank : {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_health(self):
        print("Checking plant health...")
        for plant in self.plants:
            try:
                check_plant_health(plant.name, plant.water, plant.sunlight)
            except Garden_Error as e:
                print(f"\033[31mError\033[0m checking {plant.name}: {e}")


# Test function
def main():
    print("=== Garden Management System ===\n")

    manager = GardenManager(6)

    jardin = [
        Plant("tree", 5, 13),  # Sunlight too higth
        Plant("chien", 4, 1),  # Sunlight too low
        Plant("plant", 50, 1),  # evrthing bad
        Plant(name=None, water=3, sunlight=4),  # Invalid name
        Plant("Potatoes", 3, 4),
        Plant("rutabaga", 10, 5),  # water on limmit
    ]

    # Adding plants (valid + invalid)
    manager.add_lst(jardin)
    manager.add_plant("Tomato", 5, 8)
    manager.add_plant("Lettuce", 12, 6)  # Water too high
    manager.add_plant("", 4, 5)  # Invalid name
    manager.add_plant("Carrot", 7, 12)  # Sunlight on limit

    # Watering plants
    manager.water_plants()

    # Checking health
    manager.check_health()

    # Testing recovery: simulate error
    print("\nTesting error recovery...")
    try:
        check_water_tank(0)
    except Garden_Error as e:
        print(f"\033[31mError\033[0m: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
