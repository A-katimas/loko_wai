# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 17:42:04 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/21 18:48:29 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(day = -1):
    first = False
    if day == -1:
        day = int (input("Days until harvest : "))
        first = True
    if day > 0 :
        ft_count_harvest_recursive(day-1)
        print(f"day {day}")
    if first :
        print("Harvest time!")

ft_count_harvest_recursive()