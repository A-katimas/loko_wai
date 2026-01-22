def ft_harvest_total():
    totale = 0
    for i in range(1, 4):
        totale += int(input(f"day {i} harvest: "))
    print(f"Total harvest: {totale}")


ft_harvest_total()
