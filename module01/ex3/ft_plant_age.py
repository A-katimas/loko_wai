# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/21 17:41:59 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/21 18:25:38 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    var = int(input("age de plante en jour : "))
    if var > 60:
        print("deplante la ")
    else :
        print("laisse la")

ft_plant_age()