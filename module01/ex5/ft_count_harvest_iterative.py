# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 17:42:03 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/21 18:33:18 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    var = int (input("Days until harvest:"))
    for i in range (1, var+1):
        print(f"day {i}")
    print("Harvest time!")
ft_count_harvest_iterative()