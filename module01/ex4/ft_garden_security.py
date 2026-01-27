# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42mulhouse.f    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 17:36:49 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/26 14:26:00 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
    __instance = [];
    def __init__(self, name ,starting_height ,starting_age):
        self.name = name

        self.error = self.find_error(starting_height,starting_age)
        if self.error <0:
            print(self.print_error(self.error,starting_height,starting_age))
        else:
            self.set_height(int (starting_height));
            self.set_age(int(starting_age));
            self.__class__.__instance.append(self);
            print(f"Plant Created: {self}")

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return(self.__age)

    def older(self):
        self.grow();
        self.set_age(int (self.__age) + int(1));

    def grow(self):
        self.set_height(int(self.__height) +int(1));

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

    def print_instance(self) :

        for i in range (len(self.__class__.__instance)):
            print("\nCurrent plant:",self.__class__.__instance[i].name,f"({self.__class__.__instance[i].__height}cm, {self.__class__.__instance[i].__age} days)")

    def print_error(self,error,height,age):
        debu = "Invalid operation attempted:";
        if (error == -3):
            return (debu + f"\theight {height}cm \t\033[31m[REJECTED]\033[0m\n\t\t\t\tage {age} \t\033[31m[REJECTED]\033[0m\nSecurity: Negative height and age rejected\n")
        if (error == -2):
            return(debu + f"\tage {age} \t\033[31m[REJECTED]\033[0m\nSecurity: Negative age rejected\n")
        if (error == -1):
            return(debu + f"\theight {height}cm \t\033[31m[REJECTED]\033[0m\nSecurity: Negative height rejected\n")
        return("komotuestla");

    def __repr__(self):
        if self.error == 0:
            return(f"{self.name} \nheight update {self.__height}cm\t\033[32m [OK]\033[0m\nAge updated: {self.__age} days\t\033[32m [OK]\033[0m\n\n")
        else:
            return("c'est mort tu rentre pas");


def main():
    print("=== Garden Security System ===")
    jardin = [Plant("Rose", 44, 5),
              Plant("chien",54,-34),
              Plant("enfant",-4,0),
              Plant("Void",-34,-65),
              Plant("pamplemouse",13,3)]
    jardin[0].print_instance();
if __name__ == "__main__":
    main();
