# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 17:36:49 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/22 18:48:50 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(self, name ,starting_height ,starting_age):
        self.name = name

        self.error = self.find_error(starting_height,starting_age)
        if self.error <0:
            print(self.print_error(self.error,starting_height,starting_age))
        else:
            self.__height = self.set_height(starting_height);
            self.__age = self.set_height(starting_age);
            print(f"Plant Created: {self}")

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return(self.__age)

    def older(self):
        self.grow();
        self.__age += 1;

    def grow(self):
        self.h__eight += 1;

    def set_height(self, new_height):
        self.__height = new_height;

    def set_age(self, new_age):
        self.__age = new_age

    def find_error(self, height = -1 , age = -1):
        if age < 0 and height < 0:
            return  -3;
        elif age < 0:
            return -2;
        elif height < 0:
            return -1;
        else:
            return 0;

    def print_error(self,error,height,age):
        debu = "Invalid operation attempted:";
        if (error == -3):
            return (debu + f"\nheight {height}cm [REJECTED]\nage {age} [REJECTED]\nSecurity: Negative height and age rejected")
        if (error == -2):
            return(debu + f" age {age} [REJECTED]\nSecurity: Negative age rejected")
        if (error == -1):
            return(debu + f" height {height}cm [REJECTED]\nSecurity: Negative height rejected")
        return("komotuestla");

    def __repr__(self):
        if self.error == 0:
            return(f"{self.name} \nheight update {self.__height}cm [OK]\nAge updated: {self.__age} days [OK]\n\n")
        else:
            return("c'est mort tu rentre pas");


def main():
    print("=== Garden Security System ===")
    jardin = [Plant("Rose", 44, 5),
              Plant("chien",54,-34)]

if __name__ == "__main__":
    main();
