# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 17:42:05 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/22 14:28:55 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    garden = str(input("Enter garden name:"))
    plante = int(input("Enter number of plants:"))
    print("garden : "+garden)
    print(f"plante : {plante}")
    print("Status: Growing well!")
    
ft_garden_summary()