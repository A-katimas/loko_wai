def ft_plant_age() -> None:
    var = int(input("Days since last watering: "))

    if var >= 4:
        print("Water the plants!")

    else:
        print("Plants are fine")


ft_plant_age()
