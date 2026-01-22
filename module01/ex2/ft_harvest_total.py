# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 17:41:57 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/21 18:16:27 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    totale = 0
    for i in range(1,4):
        totale += int(input(f"day {i} "))
    print(totale)

ft_harvest_total()