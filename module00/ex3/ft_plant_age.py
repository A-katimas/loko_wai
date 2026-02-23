def ft_plant_age() -> None:
    var = int(input("Enter plant age in days: "))
    if var > 60:
        print("Plant is ready to harvest!")

    else:
        print("Plant needs more time to grow.")


ft_plant_age()
