def ft_count_harvest_iterative() -> None:
    var = int(input("Days until harvest: "))

    for i in range(1, var + 1):
        print(f"day {i}")

    print("Harvest time!")


ft_count_harvest_iterative()
