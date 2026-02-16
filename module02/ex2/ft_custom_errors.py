class Garden_Error(Exception):
    def __init__(self,message: str = "Error garden"):
        super().__init__(f"{message}")

class Plant_Error(Garden_Error):
    def __init__(self ,plant):
        super().__init__(f"{plant} is not a str")

class Water_Error(Garden_Error):
    def __init__(self):
        super().__init__("not enought water in tank")

def check_water(water: int):
    if water < 10 :
        raise Water_Error()

def check_plant(plant):
    if not isinstance(plant, str):
        raise Plant_Error(plant)

def main():
    plant = 3
    water = 5

    print("=== Custom Garden Errors Demo ===\n")
    try :
        print("Testing WaterError...")
        check_water(water)
    except Water_Error as e :
        print(f"\tCaught WaterError: {e}\n")

    try :
        print("Testing PlantError...")
        check_plant(plant)
    except Plant_Error as e  :
        print(f"\tCaught PlantError: {e}\n")

    try :
        print("Testing catching all garden errors...")
        check_water(water)
    except Garden_Error as e :
        print(f"\tCaught a garden error: {e}")

    try :
        check_plant(plant)
    except Garden_Error as e :
        print(f"\tCaught a garden error: {e}\n")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    main()