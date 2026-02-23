def ft_count_harvest_recursive(day=-1) -> None:
    first = False
    if day == -1:
        day = int(input("Days until harvest : "))
        first = True
    if day > 0:
        ft_count_harvest_recursive(day - 1)
        print(f"day {day}")
    if first:
        print("Harvest time!")


ft_count_harvest_recursive()
