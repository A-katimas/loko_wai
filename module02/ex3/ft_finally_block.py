class Plant:
    instance = []

    def __init__(self, name: str, water: int):
        self.water = water
        self.name = name
        Plant.instance.append(self)

    def watering(self):
        print("watering 💧")
        error = False
        try:
            check_water(self.water)
        except Water_Error as e:
            print(e)
            error = True
        finally:
            print("Closing watering system (cleanup)")
        if error == False:
            print("Watering completed successfully!")


class Garden_Error(Exception):
    def __init__(self, message: str = "Error garden"):
        super().__init__(f"{message}")

class Water_Error(Garden_Error):
    def __init__(self):
        super().__init__("not enought water in tank")


def check_water(water: int):
    if water < 10:
        raise Water_Error()

def main():
    print("=== Garden Watering System ===\n")
    jardin = [Plant("3", 5), Plant("tomate", 50), Plant("chien", 4), Plant("plant", 50)]

    for plant in jardin:
        print(f"i'm {plant.name}")
        plant.watering()
        print("Next plant \n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
