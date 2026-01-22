# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 16:05:42 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/22 16:56:25 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self,name ,height ,age):
        self.name = name
        self.Height= height
        self.age =age

    def __repr__(self):
        return (f"{self.name}: {self.Height}cm, {self.age} days old")


def main():
    a = Plant("rose", 25, 30)
    b = Plant("Sunflower", 80, 45)
    c = Plant("Cactus",15,120)

    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    main();