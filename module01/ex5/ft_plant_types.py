# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42mulhouse.f    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 17:36:49 by jtardieu          #+#    #+#              #
#    Updated: 2026/01/26 15:15:03 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    __instance = [];

    def __init__(self, name ,starting_height ,starting_age):
        self.set_name(name)
        self.set_height(int (starting_height));
        self.set_age(int(starting_age));
        self.__class__.__instance.append(self);
        print(f"Plant Created: {self}")

    def get_name(self):
        return(self.__name)
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

    def set_name(self,name):
        self.__name = name

    def print_instance(self) :

        for i in range (len(self.__class__.__instance)):
            print("\nCurrent plant:",self.__class__.__instance[i].name,f"({self.__class__.__instance[i].__height}cm, {self.__class__.__instance[i].__age} days)")

    def __repr__(self):
        table = {"flower": f"{1} is blowmingh",
            "tree": f"{1} provide shadow ",
            "vegetabels": f"covers {1} is rich on viutamin d"}


        return("Unknown unit type")

class flower (Plant) :
    def __init__ (self ,name ,starting_height ,starting_age):
        super().set_age(starting_age) ;
        super().set_height(starting_height) ;
        super().set_name(name);
        print(f"je suis une {super().get_name()} ");

def main():
    print("=== Garden Security System ===")
    jardin = [flower("Rose", 44, 5),
              Plant("oack",150,3),
              Plant("pamplemouse",13,3)]
    jardin[0].print_instance();
if __name__ == "__main__":
    main();
